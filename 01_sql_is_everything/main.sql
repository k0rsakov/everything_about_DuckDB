-- Самый простой запрос, который поймут все
SELECT 1 AS one

-- Пользователи, которые совершали покупки (только с продажами)
SELECT
    u.user_id,
    u.name,
    u.email,
    o.order_id,
    o.order_date,
    o.amount
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id;

-- Все пользователи, включая тех, у кого нет продаж
SELECT
    u.user_id,
    u.name,
    u.email,
    o.order_id,
    o.order_date,
    o.amount
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id;

-- Только пользователи без продаж
SELECT
    u.user_id,
    u.name,
    u.email
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE o.order_id IS NULL;