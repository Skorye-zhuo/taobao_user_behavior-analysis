WITH item_stats AS (
    SELECT
        item_id,
        SUM(IF(behavior='pv', 1, 0)) AS pv_cnt,
        SUM(IF(behavior='buy', 1, 0)) AS buy_cnt
    FROM clean_user_behavior
    GROUP BY item_id
)
-- 【拆解】：再从这个临时表里，算转化率并过滤
SELECT
    item_id,
    pv_cnt,
    buy_cnt,
    ROUND(buy_cnt * 1.0 / NULLIF(pv_cnt, 0), 4) AS conv_rate
FROM item_stats
WHERE pv_cnt > 10            -- 💡 避坑：过滤掉只有几个人看的冷门商品，防假数据
ORDER BY conv_rate ASC        -- 💡 找转化最差的
LIMIT 10;
