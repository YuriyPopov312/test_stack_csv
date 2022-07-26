IF OBJECT_ID (N'dbo.select_orders_by_item_name', N'IF') IS NOT NULL
    DROP FUNCTION dbo.select_orders_by_item_name;
GO
CREATE FUNCTION dbo.select_orders_by_item_name(@string VARCHAR(255))
RETURNS TABLE
AS
RETURN
(
    SELECT O.row_id AS 'Ид. Заказа', C.name AS 'Заказчик', COUNT(O.row_id) AS 'Кол-во позиций'
    FROM Orders AS O JOIN Customers AS C ON O.customer_id = C.row_id
	JOIN OrderItems AS OI ON OI.order_id = O.row_id
    WHERE OI.name = @string
	GROUP BY O.row_id, C.name
);


