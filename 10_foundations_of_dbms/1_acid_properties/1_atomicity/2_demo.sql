-- 🧪 SQL Atomicity Demo

-- ✅ Success Case: Money transfer from Alice to Bob
BEGIN;

UPDATE account SET balance = balance - 100 WHERE name = 'Alice';
UPDATE account SET balance = balance + 100 WHERE name = 'Bob';

COMMIT;

-- ❌ Failure Case: Simulate error to trigger rollback
BEGIN;

UPDATE account SET balance = balance - 100 WHERE name = 'Alice';
UPDATE account SET balance = balance + (100 / 0) WHERE name = 'Bob'; -- force error

ROLLBACK;
