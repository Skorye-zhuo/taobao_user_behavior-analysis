SELECT
    SUM(IF(behavior = 'pv',   1, 0)) AS pv_count,
    SUM(IF(behavior = 'cart', 1, 0)) AS cart_count,
    SUM(IF(behavior = 'fav',  1, 0)) AS fav_count,
    SUM(IF(behavior = 'buy',  1, 0)) AS buy_count
FROM user_behavior;
