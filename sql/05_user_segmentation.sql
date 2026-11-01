SELECT
    user_id,
    SUM(IF(behavior = 'pv',  1, 0)) AS pv_cnt,
    SUM(IF(behavior = 'buy', 1, 0)) AS buy_cnt
FROM clean_user_behavior
GROUP BY user_id
ORDER BY user_id;
-- 3.2 只保留下单人群，按购买次数降序
SELECT
    user_id,
    SUM(IF(behavior = 'pv',  1, 0)) AS pv_cnt,
    SUM(IF(behavior = 'buy', 1, 0)) AS buy_cnt
FROM clean_user_behavior
GROUP BY user_id
HAVING buy_cnt > 0
ORDER BY buy_cnt DESC;
