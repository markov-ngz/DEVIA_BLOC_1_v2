from PostgresHandler import PostgresHandler

class TranslationLoader(PostgresHandler):

    def __init__(self, host: str, port: str, database: str, user: str, password: str) -> None:
        super().__init__(host, port, database, user, password)

    def insertSources(self)->dict:
        """
        """
        insert_query  =  "INSERT INTO public.source (type, name) VALUES ('%s','%s') ON CONFLICT DO NOTHING RETURNING id ;" 
        select_query = "SELECT id FROM public.source WHERE type = '%s' AND name = '%s' ;"


    def insertLanguages(self, pair_languages : list )->list:
        
        insert_query = "INSERT INTO public.languages (lang_origin, lang_target) VALUES ('{0}','{1}') ON CONFLICT DO NOTHING RETURNING id ;"
        select_query = "SELECT id FROM public.languages WHERE lang_origin ='{0}' AND lang_target = '{1}' ;"

        ids = []
        for pair in pair_languages : 
            format_insert = insert_query.format(pair["lang_origin"],pair["lang_target"])
            # try to insert the data
            result = self.execute_sql(format_insert)
            # if the data is already present, no id will be returned hence fetch it 
            if len(result) < 1 :
                format_select = select_query.format(pair["lang_origin"],pair["lang_target"])
                result = self.execute_sql(format_select)
            row = {"pair":(pair["lang_origin"],pair["lang_target"]),"id":result[0] }
            ids.append(row)
            
        return ids
        


