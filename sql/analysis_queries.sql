-- =========================================
-- 1. Total Sales
-- =========================================
SELECT ROUND(SUM(sales), 2) AS total_sales
FROM superstore;

-- =========================================
-- 2. Total Profit
-- =========================================
SELECT ROUND(SUM(profit), 2) AS total_profit
FROM superstore;

-- =========================================
-- 3. Total Orders
-- =========================================
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM superstore;

-- =========================================
-- 4. Total Customers
-- =========================================
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM superstore;

-- =========================================
-- 5. Sales by Category
-- =========================================
SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;

-- =========================================
-- 6. Profit by Category
-- =========================================
SELECT
    category,
    ROUND(SUM(profit), 2) AS total_profit
FROM superstore
GROUP BY category
ORDER BY total_profit DESC;

-- =========================================
-- 7. Sales by Region
-- =========================================
SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY region
ORDER BY total_sales DESC;

-- =========================================
-- 8. Top 10 Customers
-- =========================================
SELECT
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 10;

-- =========================================
-- 9. Top 10 Products
-- =========================================
SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;

-- =========================================
-- 10. Sales by Segment
-- =========================================
SELECT
    segment,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY segment
ORDER BY total_sales DESC;

-- =========================================
-- 11. Top 10 States by Sales
-- =========================================
SELECT
    state,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY state
ORDER BY total_sales DESC
LIMIT 10;

-- =========================================
-- 12. Top 10 Cities by Sales
-- =========================================
SELECT
    city,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY city
ORDER BY total_sales DESC
LIMIT 10;

-- =========================================
-- 13. Average Order Value
-- =========================================
SELECT
    ROUND(SUM(sales) / COUNT(DISTINCT order_id), 2) AS average_order_value
FROM superstore;

-- =========================================
-- 14. Sales and Profit by Ship Mode
-- =========================================
SELECT
    ship_mode,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM superstore
GROUP BY ship_mode
ORDER BY total_sales DESC;

-- =========================================
-- 15. Monthly Sales Trend
-- =========================================
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY sales_month;

-- =========================================
-- 16. Monthly Profit Trend
-- =========================================
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
    ROUND(SUM(profit), 2) AS total_profit
FROM superstore
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY sales_month;

-- =========================================
-- 17. Yearly Sales and Profit
-- =========================================
SELECT
    YEAR(order_date) AS sales_year,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM superstore
GROUP BY YEAR(order_date)
ORDER BY sales_year;

-- =========================================
-- 18. Overall Profit Margin
-- =========================================
SELECT
    ROUND(
        SUM(profit) / NULLIF(SUM(sales), 0) * 100,
        2
    ) AS profit_margin_percentage
FROM superstore;

-- =========================================
-- 19. Profit Margin by Category
-- =========================================
SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(
        SUM(profit) / NULLIF(SUM(sales), 0) * 100,
        2
    ) AS profit_margin_percentage
FROM superstore
GROUP BY category
ORDER BY profit_margin_percentage DESC;

-- =========================================
-- 20. Category Sales Contribution
-- =========================================
SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(
        SUM(sales) * 100.0 /
        SUM(SUM(sales)) OVER (),
        2
    ) AS sales_contribution_percentage
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;

-- =========================================
-- 21. Rank Categories by Sales
-- =========================================
SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    DENSE_RANK() OVER (
        ORDER BY SUM(sales) DESC
    ) AS sales_rank
FROM superstore
GROUP BY category;

-- =========================================
-- 22. Top 3 Products in Each Category
-- =========================================
WITH product_sales AS (
    SELECT
        category,
        product_name,
        SUM(sales) AS total_sales
    FROM superstore
    GROUP BY category, product_name
),
ranked_products AS (
    SELECT
        category,
        product_name,
        ROUND(total_sales, 2) AS total_sales,
        DENSE_RANK() OVER (
            PARTITION BY category
            ORDER BY total_sales DESC
        ) AS product_rank
    FROM product_sales
)
SELECT
    category,
    product_name,
    total_sales,
    product_rank
FROM ranked_products
WHERE product_rank <= 3
ORDER BY category, product_rank;

-- =========================================
-- 23. Running Total of Monthly Sales
-- =========================================
WITH monthly_sales AS (
    SELECT
        DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
        SUM(sales) AS total_sales
    FROM superstore
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT
    sales_month,
    ROUND(total_sales, 2) AS monthly_sales,
    ROUND(
        SUM(total_sales) OVER (
            ORDER BY sales_month
        ),
        2
    ) AS running_total_sales
FROM monthly_sales
ORDER BY sales_month;

-- =========================================
-- 24. Year-over-Year Sales Growth
-- =========================================
WITH yearly_sales AS (
    SELECT
        YEAR(order_date) AS sales_year,
        SUM(sales) AS total_sales
    FROM superstore
    GROUP BY YEAR(order_date)
),
yearly_comparison AS (
    SELECT
        sales_year,
        total_sales,
        LAG(total_sales) OVER (
            ORDER BY sales_year
        ) AS previous_year_sales
    FROM yearly_sales
)
SELECT
    sales_year,
    ROUND(total_sales, 2) AS total_sales,
    ROUND(previous_year_sales, 2) AS previous_year_sales,
    ROUND(
        (total_sales - previous_year_sales)
        / NULLIF(previous_year_sales, 0) * 100,
        2
    ) AS yoy_growth_percentage
FROM yearly_comparison
ORDER BY sales_year;

-- =========================================
-- 25. Classify Orders by Sales Value
-- =========================================
SELECT
    order_id,
    ROUND(SUM(sales), 2) AS order_value,
    CASE
        WHEN SUM(sales) >= 1000 THEN 'High Value'
        WHEN SUM(sales) >= 500 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS order_category
FROM superstore
GROUP BY order_id
ORDER BY order_value DESC;