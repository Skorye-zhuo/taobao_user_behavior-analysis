WITH pv_stats AS (
    SELECT category_id, COUNT(*) AS pv_num
    FROM user_behavior
    WHERE behavior = 'pv'
    GROUP BY category_id
),
buy_stats AS (
    SELECT category_id, COUNT(*) AS buy_num
    FROM user_behavior
    WHERE behavior = 'buy'
    GROUP BY category_id
)
SELECT
    p.category_id,
    p.pv_num,
    IFNULL(b.buy_num, 0) AS buy_num,
    -- 修正：使用 NULLIF 防止除零，且保留真实的 NULL 含义
    ROUND(IFNULL(b.buy_num, 0) / NULLIF(p.pv_num, 0), 4) AS convert_rate
FROM pv_stats p
LEFT JOIN buy_stats b ON p.category_id = b.category_id
ORDER BY convert_rate DESC
LIMIT 15;
