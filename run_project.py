#!/usr/bin/env python3
from pathlib import Path
import csv, sqlite3
ROOT = Path(__file__).resolve().parent
SQL, DATA, RESULTS = ROOT/"sql", ROOT/"data", ROOT/"results"
DATA.mkdir(exist_ok=True)
db = DATA/"capstone_demo.sqlite"
if db.exists(): db.unlink()
conn = sqlite3.connect(db)
try:
    conn.executescript((SQL/"00_schema_and_seed.sql").read_text(encoding="utf-8"))
    expected = {"customers":4,"products":9,"sales_reps":24,"orders":90}
    for t,n in expected.items():
        actual=conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        print(f"{t}: {actual} rows")
        assert actual == n, f"{t}: expected {n}, got {actual}"
    completed=conn.execute("SELECT COUNT(*) FROM orders WHERE status='Completed'").fetchone()[0]
    revenue=conn.execute("SELECT SUM(amount) FROM orders WHERE status='Completed'").fetchone()[0]
    units=conn.execute("SELECT SUM(units) FROM orders WHERE status='Completed'").fetchone()[0]
    print(f"completed={completed}; revenue={revenue:,.0f}; units={units}")
    assert (completed,revenue,units)==(63,346200,106)
    for name, query in [
      ("orders_enriched.csv", "\n".join(x for x in (SQL/"q09.sql").read_text().splitlines() if not x.strip().startswith("--"))),
      ("orders_clean.csv", """SELECT o.order_id,o.order_code,o.order_date,c.customer_name,p.product_name,p.category,p.unit_price,r.rep_name,o.region,o.units,o.amount,o.status,ROUND(o.amount/NULLIF(o.units,0),2) AS revenue_per_unit FROM orders o JOIN customers c ON c.customer_id=o.customer_id JOIN products p ON p.product_id=o.product_id JOIN sales_reps r ON r.rep_id=o.rep_id WHERE o.status='Completed' ORDER BY o.order_id""")
    ]:
      cur=conn.execute(query); rows=cur.fetchall()
      with (DATA/name).open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.writer(f); w.writerow([d[0] for d in cur.description]); w.writerows(rows)
      print(f"{name}: {len(rows)} rows, {len(cur.description)} columns")
    lines=["# SQL Query Results",""," > Synthetic demo data only; replace with official course data before final submission.","","## Seed check","","| Table | Rows |","|---|---:|"]
    for t,n in expected.items(): lines.append(f"| {t} | {n} |")
    lines += ["",f"- Completed orders: **{completed}**",f"- Completed revenue: **{revenue:,.0f}**",f"- Completed units: **{units}**",""]
    for i in range(1,14):
      path=SQL/f"q{i:02d}.sql"
      query="\n".join(x for x in path.read_text(encoding="utf-8").splitlines() if not x.strip().startswith("--"))
      cur=conn.execute(query); rows=cur.fetchall(); cols=[d[0] for d in cur.description]
      lines += [f"## q{i:02d}","",path.read_text(encoding="utf-8").splitlines()[0].replace("-- ",""),"",f"Row count: **{len(rows)}**","","| "+" | ".join(cols)+" |","| "+" | ".join(["---"]*len(cols))+" |"]
      for row in (rows[:5] if len(rows)>15 else rows):
        lines.append("| "+" | ".join("" if v is None else str(v) for v in row)+" |")
      if len(rows)>15: lines.append(f"\n_Showing first 5 of {len(rows)} rows._")
      lines.append("")
    (RESULTS/"query_results.md").write_text("\n".join(lines),encoding="utf-8")
    print("SUCCESS: SQL checks passed; CSVs and query results regenerated.")
finally:
    conn.close()
