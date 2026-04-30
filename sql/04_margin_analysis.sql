-- Compare margin by category using list price minus cost
SELECT
  i.category,
  COUNT(i.item_id) AS total_items,
  ROUND(AVG(i.list_price - i.cost), 2) AS avg_margin,
  ROUND(AVG((i.list_price - i.cost) * 100.0 / NULLIF(i.cost, 0)), 2) AS avg_margin_percent
FROM inventory i
GROUP BY i.category
ORDER BY avg_margin DESC;
