#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE translations ( id SERIAL CONSTRAINT firstkey PRIMARY KEY, french VARCHAR(256) NOT NULL, polish VARCHAR(256) NOT NULL);
EOSQL
