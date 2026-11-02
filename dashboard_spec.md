# Dashboard Specification

> Demo-data warning: this is a dashboard plan over synthetic data, not verified business analysis.

## Audience
Regional sales leadership.

## 13 output columns
Dimensions: order_id, order_code, order_date, customer_name, product_name, category, rep_name, region, status.
Measures: unit_price, units, amount, revenue_per_unit. IDs may also be used as drill-down dimensions.

## KPI cards
1. Completed revenue: 346,200 (demo target)
2. Completed units: 106 (demo target)

## Four charts
1. Revenue by region — bar chart.
2. Revenue by category — horizontal bar chart.
3. Monthly completed revenue — line chart.
4. Order detail — table with date, region, category, product, rep, units and revenue.

## Filters
Region, category, month, sales representative.

## Layout
Top: KPI cards. Middle: regional and category comparisons. Bottom: monthly trend and detail table.

## Recommendations to validate against official data
1. Investigate high- and low-performing regions.
2. Allocate promotions only after checking margin and demand.
3. Verify monthly anomalies before making decisions.
