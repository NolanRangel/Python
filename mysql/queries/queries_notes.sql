
-- ****USE lead_gen_business

-- IMPORT -- either copy and paste from sql file OR create ERD table and then, Database(TAB), Forward engineer, run through commands and double check port, 
-- IMPORT Cont. -- go to connections page (dolphin) and refresh SCHEMAS

-- SELECT
-- SELECT all FROM table_name WHERE conditions();
-- SELECT column_name FROM table_name WHERE condition(s) (whith conditional);
-- SELECT column_name FROM table_name ORDER BY condition(s) (whith sorting);
-- SELECT column_name FROM table_name LIMIT 3 condition(s) (whith LIMIT);
-- SELECT column_name FROM table_name LIMIT 3 OFFSET 2 (whith LIMIT and OFFSET)(returns records 3 through 5;
-- SELECT column_name FROM table_name LIMIT 3, 2 (whith LIMIT and OFFSET)(returns records 3 through 5;

-- INSERT
-- INSERT INTO table_name (column_name1, column_name2) 
-- VALUES('column1_value', 'column2_value');
-- **NUMBER OF COLUMS AND VALUES NEED TO MATCH UP**

-- UPDATE
-- UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s);

-- DELETE -- ********IMPORTANT: if WHERE condition is not added to the DELETE statement, it will delete all the records on the table.********
-- DELETE FROM table_name WHERE condition(s);

-- SQL SAFE UPDATES ERROR
-- If you are getting an error regarding SQL SAFE UPDATES, run the following command to let MySQL Workbench know that you know what you are
-- doing and you want to DELETE stuff from the database.
-- SET SQL_SAFE_UPDATES = 0;

-- MySQL Functions

-- TEXT
-- CONCAT()
-- SELECT CONCAT('MR.',' ', first_name,' ', last_name) AS full_name, email AS e FROM clients;

-- CONCAT_WS()
-- SELECT CONCAT_WS(' ', first_name, last_name) AS full_name FROM clients;

-- LENGTH()
-- SELECT LENGTH(last_name) AS last_len FROM clients;

-- LOWER()
-- SELECT LOWER(first_name) AS first_lowercase FROM clients;

-- DATE
-- HOUR()
-- SELECT HOUR(joined_datetime) AS date_hour, joined_datetime FROM clients;

-- DAYNAME()
-- SELECT DAYNAME(joined_datetime) AS day_name, joined_datetime FROM clients;

-- MONTH()
-- SELECT MONTH(joined_datetime) AS month_number, joined_datetime FROM clients;

-- NOW()
-- SELECT NOW() AS right_now;

-- DATE_FORMAT()
-- SELECT DATE_FORMAT(joined_datetime, '%W %M %e, %Y')AS date_time FROM clients;



-- JOINING TABLES

-- ONE TO ONE
-- SELECT * 
-- FROM customers 
-- JOIN addresses ON addresses.id = customers.address_id;

-- ONE TO MANY
-- SELECT * 
-- FROM orders 
-- JOIN customers ON customers.id = orders.customer_id;

-- MANY TO MANY
-- SELECT * 
-- FROM orders 
-- JOIN items_orders ON orders.id = items_orders.order_id 
-- JOIN items ON items.id = items_orders.item_id;


-- JOIN

-- **FIND all the clients (first and last name) billing amounts and charged dates

-- SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
-- FROM clients
-- JOIN billing ON clients.id = billing.clients_id;

-- **list all the domain names and leads (first and last name) for each site

-- SELECT sites.domain_name, leads.first_name, leads.last_name
-- FROM sites
-- JOIN leads ON sites.id = leads.sites_id;

-- **JOIN ON MULTIPLE TABLES
-- Get the names of the clients. their domain names and the first names of all the leads generated from those sites.

-- SELECT clients.first_name AS client_first, clients.last_name, sites.domain_name, leads.first_name AS leads_first
-- FROM clients
-- JOIN sites ON clients.id = sites.clients_id
-- JOIN leads ON sites_id = leads.sites_id;

-- **LEFT & RIGHT JOIN
-- List all the clients and the sites each client has. even if the client hasn"t landed a site yet.

-- SELECT clients.first_name, clients.last_name, sites.domain_name 
-- FROM clients
-- LEFT JOIN sites ON clients.id = sites.clients_id;

-- **GROUPING BY ROWS
-- GROUP BY
-- SUM, MIN, MAX, AVG 
-- Find all the clients (first and last name) and their total billing amounts

-- SELECT clients.first_name, clients.last_name, SUM(billing.amount) 
-- FROM clients
-- LEFT JOIN billing ON clients.id = billing.clients_id
-- GROUP BY clients.id;

-- **GROUP CONCAT
-- List all the domain names associated with each client

-- SELECT GROUP_CONCAT(' ',sites.domain_name) AS domains, clients.first_name, clients.last_name
-- FROM clients
-- JOIN sites ON clients.id = sites.clients_id
-- GROUP BY clients.id

-- **COUNT
-- Find the total number of leads for each site

-- SELECT COUNT(leads.id), sites.domain_name
-- FROM sites
-- JOIN leads ON sites.id = leads.sites_id
-- GROUP BY sites.id;