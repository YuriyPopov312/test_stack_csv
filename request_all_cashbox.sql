SELECT C.name AS 'Наименование' 
FROM Orders AS O 
JOIN Customers AS C ON O.customer_id = C.row_id
JOIN OrderItems AS OI ON OI.order_id = O.row_id
WHERE YEAR(O.registered_at) = 2020 AND OI.name = 'Кассовый аппарат'
GROUP BY C.name
HAVING COUNT(*) > 1