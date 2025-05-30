-- 🧪 SQL Consistency Demo

-- Drop previous test table if it exists
DROP TABLE IF EXISTS product;

-- ✅ Define table with constraints that ensure consistency
CREATE TABLE product (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  stock INT NOT NULL CHECK (stock >= 0),
  price NUMERIC(10,2) NOT NULL CHECK (price >= 0)
);

-- ✅ Insert valid data (passes all rules)
INSERT INTO product (name, stock, price)
VALUES
  ('Laptop', 10, 1500.00),
  ('Mouse', 50, 25.00);

-- ❌ Insert with NULL name (violates NOT NULL)
-- Rejected: name must not be null
INSERT INTO product (name, stock, price)
VALUES (NULL, 10, 500.00);

-- ❌ Insert with negative stock (violates CHECK)
-- Rejected: stock must be >= 0
INSERT INTO product (name, stock, price)
VALUES ('Monitor', -5, 200.00);

-- ❌ Insert with negative price (violates CHECK)
-- Rejected: price must be >= 0
INSERT INTO product (name, stock, price)
VALUES ('Keyboard', 10, -50.00);
