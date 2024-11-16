from PostgresHandler import PostgresHandler
from pyspark.sql import DataFrame 
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType, StringType, StructField
from SparkHandler import SparkHandler 

class TranslationLoader(PostgresHandler):

    def __init__(self, host: str, port: str, database: str, user: str, password: str) -> None:
        super().__init__(host, port, database, user, password)

    def get_hashs(self, spark :SparkHandler)->DataFrame : 
        """
        Get existing hashes from the database
        """
        query = """SELECT hash FROM translations"""
        result = self.execute_sql(query)
        hashs = [r["hash"] for r in result]
        df  =spark.session.createDataFrame(hashs,StringType()).withColumnRenamed("value","existing_hash")
        return df 
    def insertSources(self , sources : list)->dict:
        """
        """
        insert_query  =  "INSERT INTO public.source (type, name) VALUES ('{0}','{1}') ON CONFLICT DO NOTHING RETURNING id ;" 
        select_query = "SELECT id FROM public.source WHERE type = '{0}' AND name = '{1}' ;"
            
        return  self.insert_get_id(sources,insert_query,select_query,["source_type","source_columns"])

    def insertLanguages(self, pair_languages : list )->list:
        """
        """
        insert_query = "INSERT INTO public.languages (lang_origin, lang_target) VALUES ('{0}','{1}') ON CONFLICT DO NOTHING RETURNING id ;"
        select_query = "SELECT id FROM public.languages WHERE lang_origin ='{0}' AND lang_target = '{1}' ;"

        return self.insert_get_id(pair_languages,insert_query,select_query,["lang_origin","lang_target"])
    
    def insert_get_id(self, pairs: list, insert_query: str, select_query :str, columns : list)->dict : 
        """
        Return {"columns":arg.columns , "ids":[ { "pair": list[col1:str,col2:str] , "id":int }, ... ] }
        """
        response = {}
        ids = []
        for pair in pairs : 
            format_insert = insert_query.format(pair[columns[0]],pair[columns[1]])
            # try to insert the data
            result = self.execute_sql(format_insert)
            # if the data is already present, no id will be returned hence fetch it 
            if len(result) < 1 :
                format_select = select_query.format(pair[columns[0]],pair[columns[1]])
                result = self.execute_sql(format_select)
            row = {"pair":(pair[columns[0]],pair[columns[1]]),"id":result[0]["id"] }
            ids.append(row)
        response["columns"] = columns
        response["ids"] = ids
        return response

    def map_fk(self, df : DataFrame, col_id : list[dict],new_col_name: str )->DataFrame:
        """
        """
        def map_id(col1:str, col2:str)->str:
            for ex in col_id["ids"] : 
                if col1 == ex["pair"][0] and col2 == ex["pair"][1] :
                    return ex["id"]
            return None 
        
        udf_map_id = udf(map_id,IntegerType())
        df = df.withColumn(new_col_name, udf_map_id(col_id["columns"][0],col_id["columns"][1]))

        for col in col_id["columns"]  : 
            df = df.drop(col)

        return df
    
