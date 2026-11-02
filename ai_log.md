# AI-Assisted Analysis Log

> The original AI SQL answer and spreadsheet error were not included. This is a validation template, not a claim to have fixed the instructor's exact query.

## Five-part prompt
- Role: careful sales data analyst.
- Task: validate SQL and calculate completed revenue growth.
- Context: revenue includes only `Completed` orders.
- Constraints: use SQLite; keep missing amounts distinct from zero; show calculation.
- Format: query, output columns, validation checks, explanation.

## Validation
- Check join keys and join cardinality.
- Filter completed orders before summing revenue.
- Check aggregation and date grouping.
- Independently recompute totals.
- Growth % = ((current - prior) / prior) * 100.

## 38% growth claim
Must be checked using the two official comparison periods. Synthetic demo data cannot validate the official claim.

## Spreadsheet lookup error
Check spaces/case, exact-match mode, duplicate keys, missing product IDs and lookup range alignment. Record the actual correction when the original workbook is available.
