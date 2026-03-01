-- Create the employees table
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    position VARCHAR(50),
    salary DECIMAL(10,2)
);

-- Insert 5 random employees
INSERT INTO employees (id, name, position, salary) VALUES
(1, 'Alice Smith', 'Manager', 75000.00),
(2, 'Bob Johnson', 'Developer', 65000.00),
(3, 'Carol Lee', 'Designer', 60000.00),
(4, 'David Kim', 'Analyst', 58000.00),
(5, 'Eva Brown', 'Tester', 55000.00);