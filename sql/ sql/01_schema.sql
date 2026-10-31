CREATE TABLE user_behavior (
    user_id BIGINT,
    item_id BIGINT,
    category_id BIGINT,
    behavior VARCHAR(10),
    `timestamp` BIGINT, -- 建议加反引号
    time VARCHAR(30),
    `hour` INT
);
