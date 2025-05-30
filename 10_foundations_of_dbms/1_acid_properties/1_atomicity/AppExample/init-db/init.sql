-- Create a single 'account' table
CREATE TABLE IF NOT EXISTS account (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  balance NUMERIC(12, 2) NOT NULL CHECK (balance >= 0)
);

-- Seed data: Alice and Bob
INSERT INTO account (name, balance)
VALUES
  ('Alice', 1000.00),
  ('Bob', 500.00)
ON CONFLICT (name) DO NOTHING;
