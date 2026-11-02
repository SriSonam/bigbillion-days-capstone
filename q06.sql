-- Q06: Revenue by region
SELECT region, ROUND(SUM(amount),2) AS revenue FROM orders WHERE status='Completed' GROUP BY region ORDER BY revenue DESC;
