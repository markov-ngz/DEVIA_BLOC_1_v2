-- 1. Languages
-- returns the id if a new pair of languages is inserted
INSERT INTO public.languages (lang_origin, lang_target) VALUES (<>,<>) ON CONFLICT DO NOTHING RETURNING id ;
-- otherwise retrieve the id of the existing pair 
SELECT id FROM public.languages WHERE lang_origin = <> AND lang_target = <> ; 

-- 2. Source 
-- returns the id if a new source is inserted
INSERT INTO public.source (type, name) VALUES (<>,<>) ON CONFLICT DO NOTHING RETURNING id ;
-- otherwise retrieve the id of the existing source  
SELECT id FROM public.source WHERE type = <> AND name = <> ;

-- 3. Translation
INSERT INTO public.translations(text_origin, text_target, extracted_at ,languages_id, source_id)
VALUES (<>,<>,<>,<languages.id>,<source.id>) ON CONFLICT DO NOTHING ; 

