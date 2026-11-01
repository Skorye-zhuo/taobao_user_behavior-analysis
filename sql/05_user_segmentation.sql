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

WITH user_agg AS (
    SELECT
        user_id,
        SUM(IF(behavior = 'pv',  1, 0)) AS pv_cnt,
        SUM(IF(behavior = 'buy', 1, 0)) AS buy_cnt
    FROM clean_user_behavior
    GROUP BY user_id
)
SELECT
    SUM(IF(buy_cnt >  0, 1, 0)) AS buy_user_count,
    SUM(IF(buy_cnt =  0, 1, 0)) AS only_view_user_count,
    SUM(IF(buy_cnt >= 2, 1, 0)) AS repurchase_user,
    SUM(IF(buy_cnt =  1, 1, 0)) AS one_time_user
FROM user_agg;
