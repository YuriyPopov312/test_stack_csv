SELECT C.name AS 'Заказчик'
FROM Orders AS O JOIN Customers AS C ON O.customer_id = C.row_id
JOIN OrderItems AS OI ON OI.order_id = O.row_id
WHERE YEAR(O.registered_at) = 2020
GROUP BY C.name
HAVING COUNT(DISTINCT order_id) = COUNT(DISTINCT CASE WHEN OI.name = 'Кассовый аппарат' THEN order_id END)