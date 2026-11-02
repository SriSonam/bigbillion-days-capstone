-- Q02: Count orders by status
SELECT status, COUNT(*) AS order_count FROM orders GROUP BY status ORDER BY status;
