USE bank;
DELETE FROM bank.u_accounts
WHERE user_id = 414;

DELETE FROM bank.users;

USE bank;
ALTER TABLE bank.u_accounts DROP cc_num;

USE bank;
DROP TABLE liabilities;

USE bank;
TRUNCATE TABLE assets;

USE restaurant;
DROP DATABASE restaurant;

USE RE;
DELETE FROM payments WHERE paid = 1;

TRUNCATE TABLE catalog;

ALTER TABLE clients DROP property_id;
