-- Q08: Best-selling products by units
SELECT p.product_name, SUM(o.units) AS units_sold, ROUND(SUM(o.amount),2) AS revenue FROM orders o JOIN products p ON p.product_id=o.product_id WHERE o.status='Completed' GROUP BY p.product_id,p.product_name ORDER BY units_sold DESC,revenue DESC;
