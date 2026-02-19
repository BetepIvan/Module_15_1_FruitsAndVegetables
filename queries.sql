CREATE TABLE FruitsAndVegetables
(Id int IDENTITY(1,1) PRIMARY KEY,
Name nvarchar(50) UNIQUE,
Type nvarchar(10),
Color nvarchar(20),
Calories int,
Description nvarchar(100));