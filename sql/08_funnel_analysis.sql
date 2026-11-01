WITH user_behavior_level AS (
    SELECT
        user_id,
        MAX(IF(behavior='pv', 1, 0)) AS has_pv,
        MAX(IF(behavior='cart', 1, 0)) AS has_cart,
        MAX(IF(behavior='fav', 1, 0)) AS has_fav,
        MAX(IF(behavior='buy', 1, 0)) AS has_buy
    FROM clean_user_behavior
    GROUP BY user_id
)
SELECT
    SUM(has_pv)   AS pv_user_cnt,
    SUM(has_cart) AS cart_user_cnt,
    SUM(has_fav)  AS fav_user_cnt,
    SUM(has_buy)  AS buy_user_cnt
FROM user_behavior_level;
