-- Create user if it does not exist
DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_roles WHERE rolname = 'fusionhub'
   ) THEN
      CREATE ROLE fusionhub WITH LOGIN PASSWORD 'secret';
   END IF;
END
$do$;

-- Create database if it does not exist
DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database WHERE datname = 'fusionhub'
   ) THEN
      CREATE DATABASE fusionhub OWNER fusionhub;
   END IF;
END
$do$;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE fusionhub TO fusionhub;
