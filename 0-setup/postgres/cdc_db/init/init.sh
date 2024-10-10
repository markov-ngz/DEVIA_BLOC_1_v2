#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    ALTER SYSTEM SET wal_level = logical ; 
    CREATE USER CDC_USER PASSWORD 'kakarott' ; 
    ALTER ROLE CDC_USER REPLICATION LOGIN ; 
EOSQL

pg_ctl restart

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    SELECT * FROM pg_create_logical_replication_slot('translation','pgoutput') ;
    CREATE TABLE translations ( id        SERIAL CONSTRAINT firstkey PRIMARY KEY, french    VARCHAR(256) NOT NULL, polish    VARCHAR(256) NOT NULL);
    CREATE PUBLICATION cdc_translation FOR TABLE translations;  
    INSERT INTO translations(french,polish) values ('Bonjour','dzien dobry');
    SELECT * FROM pg_logical_slot_get_binary_changes('translation',NULL,NULL, 'proto_version','1','publication_names','cdc_translation'); 
EOSQL