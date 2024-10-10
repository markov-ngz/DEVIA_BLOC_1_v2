CREATE KEYSPACE IF NOT EXISTS translations WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '3' };

CREATE TABLE IF NOT EXISTS translations.pl_fr (
        id UUID PRIMARY KEY,
        src_lang text,
        target_lang text,
        src_text text,
        target_text text, 
        created_at timestamp
);

INSERT INTO store.shopping_cart
      (src_lang, target_lang, src_text,target_text,created_at)
      VALUES ('fr', 'pl','example','example',toTimeStamp(now()))