-- Q13: Revenue by region and category
SELECT o.region,p.category,ROUND(SUM(o.amount),2) AS revenue FROM orders o JOIN products p ON p.product_id=o.product_id WHERE o.status='Completed' GROUP BY o.region,p.category ORDER BY o.region,revenue DESC;
