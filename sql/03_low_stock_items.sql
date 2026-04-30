-- Spot older in-stock items that might be slow-moving inventory
SELECT
  item_id,
  product_name,
  category,
  brand,
  date_added,
  status
FROM inventory
WHERE status = 'In Stock'
  AND date_added < '2026-02-15'
ORDER BY date_added ASC;
