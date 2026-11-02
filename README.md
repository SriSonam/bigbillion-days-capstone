# Big Billion Days Regional Performance Review

## Important data note
The uploaded brief provided validation targets but not the original seed script, full data, exact 13 SQL questions, AI answer, or spreadsheet workbook. This repository therefore includes a **synthetic runnable demo** matching the visible counts and totals. It is for demonstrating code flow and must be replaced/recomputed with official course data before presenting results as factual business findings.

## Tools
SQLite, Python 3.10+, VS Code, CSV/Google Sheets, Git/GitHub. Dashboard design is documented for Tableau Public.

## Run
From this folder run:
```bash
python run_project.py
```
No third-party Python packages are required. The script creates a SQLite database, runs the reporting queries, exports CSVs, and regenerates query results.

## Folder map
- `sql/00_schema_and_seed.sql`: demo schema/data
- `sql/q01.sql`–`q13.sql`: demo reporting queries
- `sql/d1_corrected.sql`: monthly comparison template
- `data/orders_enriched.csv`: 90 rows, 10 columns
- `data/orders_clean.csv`: 63 rows, 13 columns
- `results/query_results.md`: query results and row counts
- `docs/spreadsheet_notes.md`: cleaning and pivots
- `docs/dashboard_spec.md`: dashboard plan
- `docs/ai_log.md`: AI validation template

## Demo validation targets
Seed counts 4/9/24/90; completed orders 63; completed revenue 346,200; completed units 106.
