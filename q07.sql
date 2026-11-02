-- Q07: Revenue by product category
SELECT p.category, ROUND(SUM(o.amount),2) AS revenue FROM orders o JOIN products p ON p.product_id=o.product_id WHERE o.status='Completed' GROUP BY p.category ORDER BY revenue DESC;
