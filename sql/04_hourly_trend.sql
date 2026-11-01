SELECT
    `hour`,
    SUM(IF(behavior = 'pv',  1, 0)) AS pv_total,
    SUM(IF(behavior = 'buy', 1, 0)) AS buy_total,
    -- 修正：* 1.0 强制浮点运算，NULLIF 防除零
    ROUND(
        SUM(IF(behavior = 'buy', 1, 0)) * 1.0
        / NULLIF(SUM(IF(behavior = 'pv', 1, 0)), 0),
        4
    ) AS hour_convert_rate
FROM clean_user_behavior
GROUP BY `hour`
ORDER BY `hour` ASC;
