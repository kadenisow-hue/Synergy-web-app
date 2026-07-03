-- Создание базы данных для Веб-приложения "Учет задач сотрудников"
CREATE DATABASE CorporateWebDB;
GO
USE CorporateWebDB;
GO

-- Таблица должностей
CREATE TABLE Positions (
    PositionID INT IDENTITY(1,1) PRIMARY KEY,
    Title NVARCHAR(100) NOT NULL,
    Department NVARCHAR(100) NOT NULL
);

-- Таблица сотрудников
CREATE TABLE Employees (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PositionID INT FOREIGN KEY REFERENCES Positions(PositionID)
);

-- Таблица корпоративных задач
CREATE TABLE Tasks (
    TaskID INT IDENTITY(1,1) PRIMARY KEY,
    TaskTitle NVARCHAR(150) NOT NULL,
    Description NVARCHAR(MAX),
    Status NVARCHAR(50) DEFAULT 'New',
    CreatedAt DATETIME DEFAULT GETDATE(),
    EmployeeID INT FOREIGN KEY REFERENCES Employees(EmployeeID) ON DELETE SET NULL
);
GO
