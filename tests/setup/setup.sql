-- This project doesn't have any migration since 
-- tables are handled from other microservice.
CREATE TABLE daily_credit_card_aggregation (
    id SERIAL PRIMARY KEY,
    credit_card_id INT NOT NULL,
    amount REAL NOT NULL,
    aggregation_count INT NOT NULL,
    aggregation_date DATE NOT NULL,
    UNIQUE(credit_card_id, aggregation_date)
);

SELECT SETVAL('daily_credit_card_aggregation_id_seq', 1000);

INSERT INTO daily_credit_card_aggregation
  (id, credit_card_id, amount, aggregation_count, aggregation_date)
VALUES 
  (1, 100, 1500, 13, '2025-01-03'),
  (2, 100, 750, 22, '2025-01-04'),
  (3, 101, 1000, 34, '2025-01-03');


CREATE TABLE daily_user_aggregation (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    amount REAL NOT NULL,
    aggregation_count INT NOT NULL,
    aggregation_date DATE NOT NULL,
    UNIQUE(user_id, aggregation_date)
);

SELECT SETVAL('daily_user_aggregation_id_seq', 1000);

INSERT INTO daily_user_aggregation 
  (id, user_id, amount, aggregation_count, aggregation_date)
VALUES 
  (1, 100, 1500, 13, '2025-01-03'),
  (2, 100, 750, 22, '2025-01-04'),
  (3, 101, 1000, 34, '2025-01-03');

