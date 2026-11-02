-- Q09: Enriched order export
SELECT o.order_id,o.order_code,o.order_date,c.customer_name,p.product_name,p.category,r.rep_name,o.region,o.units,o.amount FROM orders o JOIN customers c ON c.customer_id=o.customer_id JOIN products p ON p.product_id=o.product_id JOIN sales_reps r ON r.rep_id=o.rep_id ORDER BY o.order_id;
