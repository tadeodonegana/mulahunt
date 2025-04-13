-- Insert sample transactions for multiple users
INSERT INTO transactions (user_id, amount, timestamp, description) VALUES
(1, 100.00, '2025-03-01 10:00:00', 'ATM Deposit'),
(1, 200.00, '2025-03-05 15:30:00', 'Online Purchase');

INSERT INTO transactions (user_id, amount, timestamp, description) VALUES
(2, 50.00, '2025-03-10 09:00:00', 'Transfer out'),
(2, 45.00, '2025-03-10 09:15:00', 'Transfer out'),
(2, 60.00, '2025-03-10 09:30:00', 'Transfer out'),
(2, 55.00, '2025-03-10 09:45:00', 'Transfer out'),
(2, 50.00, '2025-03-10 10:00:00', 'Transfer in'),
(2, 50.00, '2025-03-10 10:15:00', 'Transfer in'),
(2, 50.00, '2025-03-10 10:30:00', 'Transfer in'),
(2, 50.00, '2025-03-10 10:45:00', 'Transfer in'),
(2, 50.00, '2025-03-10 11:00:00', 'Transfer out'),
(2, 50.00, '2025-03-10 11:15:00', 'Transfer out');

INSERT INTO transactions (user_id, amount, timestamp, description) VALUES
(3, 15000.00, '2025-03-08 12:00:00', 'Wire Transfer'),
(3, 20000.00, '2025-03-08 12:05:00', 'Wire Transfer'),
(3, 500.00,   '2025-03-12 16:00:00', 'Bill Payment');

INSERT INTO transactions (user_id, amount, timestamp, description) VALUES
(4, 500.00, '2025-03-02 08:00:00', 'Salary Credit'),
(4, 300.00, '2025-03-15 14:20:00', 'Grocery Shopping'),
(4, 450.00, '2025-03-20 09:45:00', 'Utility Payment'),
(4, 600.00, '2025-03-25 18:10:00', 'Rent Transfer'),
(4, 400.00, '2025-03-28 11:30:00', 'Restaurant');

INSERT INTO transactions (user_id, amount, timestamp, description) VALUES
(5, 1000.00, '2025-03-10 10:00:00', 'Account Funding');
