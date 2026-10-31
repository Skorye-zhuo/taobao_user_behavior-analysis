WITH user_agg AS (
    SELECT
        user_id,
        SUM(IF(behavior = 'pv',  1, 0)) AS pv_cnt,
        SUM(IF(behavior = 'buy', 1, 0)) AS buy_cnt
    FROM user_behavior
    GROUP BY user_id
)
SELECT
    -- 购买/仅浏览用户统计
    SUM(IF(buy_cnt >  0, 1, 0)) AS buy_user_count,
    SUM(IF(buy_cnt =  0, 1, 0)) AS only_view_user_count,
    -- 复购/一次性用户统计
    SUM(IF(buy_cnt >= 2, 1, 0)) AS repurchase_user,
    SUM(IF(buy_cnt =  1, 1, 0)) AS one_time_user
FROM user_agg;
