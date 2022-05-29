SELECT MIN(stock) FROM e_store.products;
SELECT MIN(stock) AS min_stock FROM e_store.products;
SELECT MIN(stock) AS min_stock FROM e_store.products
WHERE id > 3;

SELECT MAX(created_at) AS newest_product FROM e_store.products;
SELECT MIN(created_at) AS oldest_product FROM e_store.products;
SELECT MIN(STOCK) AS least_stock, MAX(created_at) AS newest_product, MAX(price) AS product_max_price FROM e_store.products;

USE e_store;
SELECT products.id AS id, products.name AS product_name, products.price AS price, reviews.stars AS stars FROM products 
JOIN reviews
ON products.id = reviews.product_id
WHERE products.id = 3 OR products.id = 4;

USE e_store;
SELECT SUM(stock) AS total_stock FROM products;
SELECT product_id AS id, SUM(stars) AS total_stars FROM reviews WHERE product_id = 4;


USE e_store;
SELECT COUNT(stock) AS total_product_count FROM products;
SELECT product_id AS id, COUNT(stars) AS stars_fields_count FROM reviews WHERE product_id = 4;

USE e_store;
SELECT products.id, AVG(stars) AS avg_rating
FROM products 
JOIN reviews 
ON products.id = reviews.product_id 
WHERE product_id = 4;

USE e_store;
SELECT products.name, products.price, products.stock, AVG(stars) AS avg_stars 
FROM products 
JOIN reviews 
ON products.id = reviews.product_id 
GROUP BY products.name HAVING avg_stars BETWEEN 3.5 AND 5
ORDER BY products.id ASC;
