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

-- Duplicate constraints to ease the insertion

ALTER TABLE public.translations
ADD CONSTRAINT unique_constraint_name UNIQUE (text_origin, text_target, languages_id);

ALTER TABLE translations ADD COLUMN hash VARCHAR ;

CREATE OR REPLACE FUNCTION hash_update_tg() RETURNS trigger AS $$
BEGIN
    IF tg_op = 'INSERT' OR tg_op = 'UPDATE' THEN
        NEW.hash = md5(NEW.text_origin || NEW.text_target || NEW.languages_id)::VARCHAR;
        RETURN NEW;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER translations_compute_hash 
BEFORE INSERT OR UPDATE ON translations 
FOR EACH ROW EXECUTE PROCEDURE hash_update_tg();

ALTER TABLE public.languages
ADD CONSTRAINT unique_constraint_language UNIQUE (lang_origin, lang_target);

ALTER TABLE public.source
ADD CONSTRAINT unique_constraint_source UNIQUE (type, name);

CREATE OR REPLACE VIEW translation_view
AS
SELECT DISTINCT
    t.id,
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