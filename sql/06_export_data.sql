SELECT
    user_id,
    SUM(IF(behavior = 'buy', 1, 0)) AS buy_cnt
FROM user_behavior
GROUP BY user_id
ORDER BY buy_cnt;
