# SQL Query Results

 > Synthetic demo data only; replace with official course data before final submission.

## Seed check

| Table | Rows |
|---|---:|
| customers | 4 |
| products | 9 |
| sales_reps | 24 |
| orders | 90 |

- Completed orders: **63**
- Completed revenue: **346,200**
- Completed units: **106**

## q01

Q01: Count all orders

Row count: **1**

| total_orders |
| --- |
| 90 |

## q02

Q02: Count orders by status

Row count: **3**

| status | order_count |
| --- | --- |
| Completed | 63 |
| Disputed | 10 |
| Pending | 17 |

## q03

Q03: Completed revenue

Row count: **1**

| total_revenue |
| --- |
| 346200.0 |

## q04

Q04: Completed order count

Row count: **1**

| completed_orders |
| --- |
| 63 |

## q05

Q05: Completed units

Row count: **1**

| total_units |
| --- |
| 106 |

## q06

Q06: Revenue by region

Row count: **4**

| region | revenue |
| --- | --- |
| East | 100200.0 |
| South | 91000.0 |
| North | 79000.0 |
| West | 76000.0 |

## q07

Q07: Revenue by product category

Row count: **9**

| category | revenue |
| --- | --- |
| Accessories | 49200.0 |
| Sports | 43000.0 |
| Books | 43000.0 |
| Appliances | 43000.0 |
| Grocery | 42000.0 |
| Beauty | 42000.0 |
| Home | 28000.0 |
| Fashion | 28000.0 |
| Electronics | 28000.0 |

## q08

Q08: Best-selling products by units

Row count: **9**

| product_name | units_sold | revenue |
| --- | --- | --- |
| Product 07 | 12 | 43000.0 |
| Product 06 | 12 | 43000.0 |
| Product 05 | 12 | 42000.0 |
| Product 04 | 12 | 42000.0 |
| Product 03 | 12 | 28000.0 |
| Product 02 | 12 | 28000.0 |
| Product 01 | 12 | 28000.0 |
| Product 09 | 11 | 49200.0 |
| Product 08 | 11 | 43000.0 |

## q09

Q09: Enriched order export

Row count: **90**

| order_id | order_code | order_date | customer_name | product_name | category | rep_name | region | units | amount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ORD001 | 2026-01-01 | Aarav Retail | Product 01 | Electronics | Rep 01 | North | 2 | 3000.0 |
| 2 | ORD002 | 2026-02-02 | Meera Stores | Product 02 | Home | Rep 02 | South | 2 | 3000.0 |
| 3 | ORD003 | 2026-03-03 | Kavin Mart | Product 03 | Fashion | Rep 03 | East | 2 | 3000.0 |
| 4 | ORD004 | 2026-04-04 | Diya Traders | Product 04 | Beauty | Rep 04 | West | 2 | 3000.0 |
| 5 | ORD005 | 2026-05-05 | Aarav Retail | Product 05 | Grocery | Rep 05 | North | 2 | 3000.0 |

_Showing first 5 of 90 rows._

## q10

Q10: Sales representative performance

Row count: **24**

| rep_name | region | sales_target | completed_revenue | target_status |
| --- | --- | --- | --- | --- |
| Rep 15 | East | 100000.0 | 32200.0 | Below target |
| Rep 10 | South | 100000.0 | 26000.0 | Below target |
| Rep 11 | East | 100000.0 | 26000.0 | Below target |
| Rep 12 | West | 100000.0 | 26000.0 | Below target |
| Rep 13 | North | 100000.0 | 26000.0 | Below target |

_Showing first 5 of 24 rows._

## q11

Q11: Monthly revenue trend

Row count: **6**

| month | revenue |
| --- | --- |
| 2026-01 | 59000.0 |
| 2026-02 | 59000.0 |
| 2026-03 | 66200.0 |
| 2026-04 | 54000.0 |
| 2026-05 | 54000.0 |
| 2026-06 | 54000.0 |

## q12

Q12: Orders with missing amounts

Row count: **6**

| order_id | order_code | status | amount |
| --- | --- | --- | --- |
| 65 | ORD065 | Pending |  |
| 70 | ORD070 | Pending |  |
| 75 | ORD075 | Pending |  |
| 80 | ORD080 | Pending |  |
| 85 | ORD085 | Disputed |  |
| 90 | ORD090 | Disputed |  |

## q13

Q13: Revenue by region and category

Row count: **36**

| region | category | revenue |
| --- | --- | --- |
| East | Accessories | 27200.0 |
| East | Grocery | 21000.0 |
| East | Sports | 9000.0 |
| East | Electronics | 9000.0 |
| East | Home | 8000.0 |

_Showing first 5 of 36 rows._
