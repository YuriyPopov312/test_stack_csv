IF OBJECT_ID (N'dbo.calculate_total_price_for_orders_group', N'FN') IS NOT NULL
    DROP FUNCTION calculate_total_price_for_orders_group;
GO
CREATE FUNCTION [dbo].[calculate_total_price_for_orders_group](@row_id int)
RETURNS int
AS
-- Returns the stock level for the product.
BEGIN
    DECLARE @sum_price int;
    WITH cte_orders (row_id,parent_id,group_name) AS
	(SELECT row_id,parent_id,group_name 
	FROM Orders 
	WHERE row_id=@row_id
	UNION ALL
	SELECT O.row_id,O.parent_id,O.group_name
    FROM Orders AS O JOIN cte_orders ON O.parent_id=cte_orders.row_id)
	SELECT @sum_price = SUM(OI.price) 
	FROM cte_orders JOIN OrderItems AS OI ON cte_orders.row_id=OI.order_id
	WHERE cte_orders.group_name IS NULL
	RETURN @sum_price;
END;
