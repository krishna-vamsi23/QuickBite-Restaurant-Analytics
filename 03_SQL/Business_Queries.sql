USE QuickBite;
GO

/*==========================================================
    QUERY 1 - Executive KPIs
==========================================================*/

SELECT
    COUNT(OrderID) AS TotalOrders,
    SUM(TotalAmount) AS TotalRevenue,
    AVG(TotalAmount) AS AverageOrderValue
FROM Orders;
GO

/*==========================================================
    QUERY 2 - Total Customers
==========================================================*/

SELECT
    COUNT(CustomerID) AS TotalCustomers
FROM Customers;
GO

/*==========================================================
    QUERY 3 - Revenue by Store
==========================================================*/

SELECT
    s.StoreID,
    s.StoreName,
    SUM(o.TotalAmount) AS Revenue
FROM Orders o
JOIN Stores s
    ON o.StoreID = s.StoreID
GROUP BY
    s.StoreID,
    s.StoreName
ORDER BY Revenue DESC;
GO

/*==========================================================
    QUERY 4 - Top 10 Customers
==========================================================*/

SELECT TOP 10

    c.CustomerID,
    c.FirstName,
    c.LastName,

    SUM(o.TotalAmount) AS TotalSpent

FROM Customers c

JOIN Orders o

ON c.CustomerID = o.CustomerID

GROUP BY

    c.CustomerID,
    c.FirstName,
    c.LastName

ORDER BY TotalSpent DESC;
GO

/*==========================================================
    QUERY 5 - Monthly Revenue
==========================================================*/

SELECT

    YEAR(OrderDate) AS Year,
    MONTH(OrderDate) AS Month,

    SUM(TotalAmount) AS Revenue

FROM Orders

GROUP BY

    YEAR(OrderDate),
    MONTH(OrderDate)

ORDER BY
    Year,
    Month;
GO

/*==========================================================
    QUERY 6 - Top 10 Selling Products
==========================================================*/

SELECT TOP 10

    p.ProductID,
    p.ProductName,

    SUM(oi.Quantity) AS TotalQuantitySold,

    SUM(oi.Quantity * oi.UnitPrice) AS Revenue

FROM OrderItems oi

JOIN Products p

ON oi.ProductID = p.ProductID

GROUP BY

    p.ProductID,
    p.ProductName

ORDER BY Revenue DESC;
GO

/*==========================================================
    QUERY 7 - Revenue by Category
==========================================================*/

SELECT

    p.Category,

    SUM(oi.Quantity * oi.UnitPrice) AS Revenue

FROM OrderItems oi

JOIN Products p

ON oi.ProductID = p.ProductID

GROUP BY

    p.Category

ORDER BY Revenue DESC;
GO

/*==========================================================
    QUERY 8 - Sales by Hour
==========================================================*/

SELECT

    DATEPART(HOUR, OrderTime) AS SalesHour,

    COUNT(OrderID) AS TotalOrders,

    SUM(TotalAmount) AS Revenue

FROM Orders

GROUP BY

    DATEPART(HOUR, OrderTime)

ORDER BY SalesHour;
GO

/*==========================================================
    QUERY 9 - Average Order Value by Store
==========================================================*/

SELECT

    s.StoreName,

    AVG(o.TotalAmount) AS AverageOrderValue

FROM Orders o

JOIN Stores s

ON o.StoreID = s.StoreID

GROUP BY

    s.StoreName

ORDER BY AverageOrderValue DESC;
GO

/*==========================================================
    QUERY 10 - Employee Performance
==========================================================*/

SELECT TOP 10

    e.EmployeeID,
    e.FirstName,
    e.LastName,

    COUNT(o.OrderID) AS TotalOrders,

    SUM(o.TotalAmount) AS Revenue

FROM Employees e

JOIN Orders o

ON e.EmployeeID = o.EmployeeID

GROUP BY

    e.EmployeeID,
    e.FirstName,
    e.LastName

ORDER BY Revenue DESC;
GO

/*==========================================================
    QUERY 11 - Top Performing Stores
==========================================================*/

SELECT

    s.StoreName,

    COUNT(o.OrderID) AS TotalOrders,

    SUM(o.TotalAmount) AS Revenue

FROM Stores s

JOIN Orders o

ON s.StoreID = o.StoreID

GROUP BY

    s.StoreName

ORDER BY Revenue DESC;
GO

/*==========================================================
    QUERY 12 - Loyalty Members vs Non-Loyalty Members
==========================================================*/

SELECT

    LoyaltyMember,

    COUNT(CustomerID) AS Customers

FROM Customers

GROUP BY LoyaltyMember;
GO

/*==========================================================
    QUERY 13 - Orders by Day of Week
==========================================================*/

SELECT

    DATENAME(WEEKDAY, OrderDate) AS DayName,

    COUNT(OrderID) AS TotalOrders,

    SUM(TotalAmount) AS Revenue

FROM Orders

GROUP BY DATENAME(WEEKDAY, OrderDate)

ORDER BY Revenue DESC;
GO

/*==========================================================
    QUERY 14 - Most Popular Products
==========================================================*/

SELECT TOP 10

    p.ProductName,

    SUM(oi.Quantity) AS QuantitySold

FROM OrderItems oi

JOIN Products p

ON oi.ProductID = p.ProductID

GROUP BY

    p.ProductName

ORDER BY QuantitySold DESC;
GO

/*==========================================================
    QUERY 15 - Store Ranking
==========================================================*/

SELECT

    s.StoreName,

    SUM(o.TotalAmount) AS Revenue,

    RANK() OVER
    (
        ORDER BY SUM(o.TotalAmount) DESC
    ) AS StoreRank

FROM Stores s

JOIN Orders o

ON s.StoreID = o.StoreID

GROUP BY

    s.StoreName;
GO
