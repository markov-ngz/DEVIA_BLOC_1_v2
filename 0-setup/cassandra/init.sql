CREATE KEYSPACE IF NOT EXISTS translations WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '3' };

CREATE TABLE IF NOT EXISTS translations.pl_fr (
        id UUID PRIMARY KEY,
        src_lang text,
        target_lang text,
        src_text text,
        target_text text, 
        created_at timestamp
);

BEGIN BATCH 
INSERT INTO translations.pl_fr (id, src_lang, target_lang, src_text,target_text,created_at) VALUES (uuid(),'fr', 'pl','Le roti de madame, est-il bien cuit ?','Czy roti Madam jest dobrze ugotowane?',toTimeStamp(now())) ; 
INSERT INTO translations.pl_fr (id, src_lang, target_lang, src_text,target_text,created_at) VALUES(uuid(),'fr', 'pl','Après les carottes, coupez délicatement le melon','Po marchewce ostrożnie pokrój melona',toTimeStamp(now())) ; 
INSERT INTO translations.pl_fr (id, src_lang, target_lang, src_text,target_text,created_at) VALUES(uuid(),'fr', 'pl',' Le diable champêtre se balade en bermuda','Wiejski diabeł chodzi w bermudach',toTimeStamp(now())) ; 
INSERT INTO translations.pl_fr (id, src_lang, target_lang, src_text,target_text,created_at) VALUES(uuid(),'fr', 'pl','Voyager, c est profiter !','Podróżowanie sprawia przyjemność!',toTimeStamp(now())) ;
INSERT INTO translations.pl_fr (id, src_lang, target_lang, src_text,target_text,created_at) VALUES(uuid(),'fr', 'pl','Votre jeu de paume m épate , mon cher ami !','Twoja gra w tenisa mnie zadziwia, mój drogi przyjacielu!',toTimeStamp(now())) ;
APPLY BATCH ; 
