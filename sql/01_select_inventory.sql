-- Select all currently available inventory
SELECT
  item_id,
  product_name,
  category,
  brand,
  size,
  condition,
  list_price,
  status
FROM inventory
WHERE status = 'In Stock'
ORDER BY list_price DESC;
