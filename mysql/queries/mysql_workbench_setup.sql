USE twitter;

SELECT * FROM tweets;

SELECT first_name FROM users;
SELECT first_name FROM users where id > 2;
SELECT first_name FROM users LIMIT 1;

INSERT INTO users(first_name, last_name, created_at, updated_at)
VALUES('Nolan', 'Rangel', NOW(), NOW());
SELECT * FROM users;

UPDATE tweets SET tweet = 'Take me to your leader', created_at = NOW(), updated_at = NOW() WHERE id = 1;


DELETE FROM tweets WHERE id > 12; 
