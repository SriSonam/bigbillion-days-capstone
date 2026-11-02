-- Q11: Monthly revenue trend
SELECT substr(order_date,1,7) AS month,ROUND(SUM(amount),2) AS revenue FROM orders WHERE status='Completed' GROUP BY substr(order_date,1,7) ORDER BY month;
