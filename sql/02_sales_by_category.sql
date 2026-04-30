-- Find which product categories generated the most revenue
SELECT
  i.category,
  COUNT(s.sale_id) AS units_sold,
  SUM(s.sale_price) AS total_revenue,
  ROUND(AVG(s.sale_price), 2) AS avg_sale_price
FROM sales s
JOIN inventory i ON i.item_id = s.item_id
GROUP BY i.category
ORDER BY total_revenue DESC;
