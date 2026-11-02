-- Q12: Orders with missing amounts
SELECT order_id,order_code,status,amount FROM orders WHERE amount IS NULL ORDER BY order_id;
