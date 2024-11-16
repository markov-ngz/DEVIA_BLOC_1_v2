from JsonLogger import JsonLogger
from SparkHandler import SparkHandler 
from Settings import settings
from TranslationLoader import TranslationLoader
from pyspark.sql import Row
from pyspark.sql.functions import localtimestamp
import io 

class Main():

    app_name : str =  "hadoop_load"

    def __init__(self) -> None:
        """
        
        """
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)

        # 1. Get clean data 
        spark = SparkHandler(self.app_name)
        spark.set_filesystem()
        df = spark.get_dataframes([settings.hdfs_folder],header=True,delimiter="\t", aggregate=True)

        # 2. Get langues and sources 
        distinct_langs : list[Row] = df.select('lang_origin','lang_target').distinct().collect()
        distinct_source : list[Row] = df.select('source_columns','source_type').distinct().collect()

        loader = TranslationLoader(settings.database_hostname, settings.database_port,settings.database_name ,settings.database_username, settings.database_password)
        loader.connect()

        languages_ids = loader.insertLanguages(distinct_langs)
        sources_ids = loader.insertSources(distinct_source)
        
        # 3. Map the languages and the source to the DataFrame 
        df = loader.map_fk(df,languages_ids,"languages_id")
        df = loader.map_fk(df,sources_ids,"source_id")
        print(df.count())
        df = df.withColumn("extracted_at",localtimestamp()).drop_duplicates(["text_origin","text_target","languages_id"])
        print(df.count())
        # 4. Write DataFrame to Target Database
        # 4.1 DataFrame -> buffer
        pd = df.toPandas().drop_duplicates(["text_origin","text_target","languages_id"])
        pd.to_csv("temp_file.csv",sep="|",index=False,header=False, quotechar="}") # Ugly Loading as loading the dataframe into a buffer BytesIO object did not work 
        loader.copy_csv("public.translations","|",hquote="}",file_path="temp_file.csv") 

        

if __name__ == "__main__":
    Main()