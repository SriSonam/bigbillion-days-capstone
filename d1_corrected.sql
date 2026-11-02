-- Demo monthly query; original assignment's AI answer was not provided.
SELECT substr(order_date,1,7) AS month, ROUND(SUM(amount),2) AS completed_revenue
FROM orders
WHERE status='Completed'
GROUP BY substr(order_date,1,7)
ORDER BY month
LIMIT 2;
