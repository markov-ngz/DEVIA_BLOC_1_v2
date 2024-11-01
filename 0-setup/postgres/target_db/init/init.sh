#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE public.source
    (
        id serial,
        type character varying(256),
        name character varying(1024),
        PRIMARY KEY (id)
    );

    CREATE TABLE public.languages
    (
        id serial,
        lang_origin character varying(256),
        lang_target character varying(1024),
        PRIMARY KEY (id)
    );
    CREATE  TABLE public.translations
    (
        id serial,
        text_origin character varying(1024),
        text_target character varying(1024),
        extracted_at date,
        languages_id integer,
        source_id integer,
        PRIMARY KEY (id),
        CONSTRAINT source_id FOREIGN KEY (source_id)
            REFERENCES public.source (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
            NOT VALID,
        CONSTRAINT languages_id FOREIGN KEY (languages_id)
            REFERENCES public.languages (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
            NOT VALID
    );

    CREATE OR REPLACE VIEW translation_view
    AS
    SELECT DISTINCT
        l.lang_origin,
        l.lang_target,
        text_origin,
        text_target,
        extracted_at,
        s.type as source_type,
        s.name as source_name
    FROM translations t
    LEFT JOIN source s ON s.id = t.source_id
    LEFT JOIN languages l ON l.id = t.languages_id
    ;
EOSQL