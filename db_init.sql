CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary NUMERIC,
    join_date DATE
);

INSERT INTO employees (name, department, salary, join_date) VALUES
('Alice', 'Engineering', 95000, '2022-01-10'),
('Bob', 'Engineering', 87000, '2021-05-14'),
('Charlie', 'Sales', 65000, '2023-02-01'),
('David', 'HR', 72000, '2020-07-23'),
('Eve', 'Sales', 68000, '2022-11-15');
