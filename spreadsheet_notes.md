# Spreadsheet Cleaning Notes

> Demo-data warning: the original dataset/workbook was not included with the assignment brief.

- Import `data/orders_enriched.csv` into Google Sheets.
- Preserve dates as ISO `YYYY-MM-DD` text.
- Keep missing amounts blank; do not silently replace them with zero.
- Standardize names and trim whitespace.
- Filter to `Completed` orders.
- Pivot 1: rows = region; values = SUM of amount.
- Pivot 2: rows = category, columns = region; values = SUM of amount.
- Demo validation: 63 completed rows, 13 columns, revenue 346,200, units 106.
- Recompute all values using official course data before submission.
