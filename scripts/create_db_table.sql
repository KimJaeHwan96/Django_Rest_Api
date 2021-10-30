CREATE DATABASE rest_api_db;
CREATE USER jhkim WITH PASSWORD 'djangorestapi';
GRANT ALL PRIVILEGES ON DATABASE rest_api_db TO jhkim;
ALTER ROLE jhkim SET client_encoding TO 'utf8';
ALTER ROLE jhkim SET default_transaction_isolation TO 'read committed';
ALTER ROLE jhkim WITH SUPERUSER;