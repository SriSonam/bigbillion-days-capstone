-- Q03: Completed revenue
SELECT ROUND(SUM(amount),2) AS total_revenue FROM orders WHERE status='Completed';
