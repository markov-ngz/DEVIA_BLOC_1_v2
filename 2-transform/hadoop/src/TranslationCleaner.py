from pyspark.sql import DataFrame
from pyspark.sql.functions import length , col 
from JsonLogger import JsonLogger

class TranslationCleaner():

    def __init__(self) -> None:
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)


    def clean(self,dfs:dict)->DataFrame:
        """
        Clean the given spark.DataFrames and then Aggregate it 
        NOTE : would be nice to save errors in a DataFrame to then save for later inspection 
        """
        for path, df  in dfs.items() :
            file_statistics  = {"file":path}
            # Format columns
            try :  
                df = self.format_columns(df)
                # Count null lines 
                file_statistics["count_na"] = df.select("text_origin","text_target","lang_origin","lang_target").na.count()
                # Drop them 
                df = df.dropna(subset=["text_origin","text_target","lang_origin","lang_target"])
                # df = df.filter(length(col("text_origin")) > 2).filter(length(col("text_target")) > 2)
                df.show()
                break ; 
            except Exception as e :
                self.logger.error(str(e)) 
            finally : 
                self.logger.info(file_statistics)

    def format_column(self,columns_names: list[str], output_column : str , df : DataFrame, raise_on_not_found : bool = False ) -> DataFrame :
        """
        If a the dataframe has a column in the given column list of names  \n 
        Then it rename it 
        If the column is not found , the dataframe is returned or an exception can be raised with argument raise_on_not_found
        """    
        for col in df.columns : 
            if col in columns_names : 
                self.logger.info(f"Renamed column {col} to {output_column}")
                return df.withColumnRenamed(col, output_column)
        if raise_on_not_found : 
            raise ValueError("DataFrame do not contain columns : {0} . Got : {1}".format(columns_names , df.columns))
        else : 
            return df 
    
    def format_columns(self,df:DataFrame)->DataFrame :
        """ 
        Standardize the columns name to the expected format \n
        NOTE : the process is really not robust 
                as if the project was well conceived the entry data should already have a defined format     
        """
        
        text_origin_columns = {"raw_columns":["text_source","source_text","text_origin","origin_text","from","from_text","text_from"] , "formatted":"text_origin"}
        text_target_columns = {"raw_columns":["to_text","text_to","to","target_text","text_target"],"formatted":"text_target"}
        lang_origin_columns = {"raw_colums":["lang_origin","lang_source","source_lang"], "formatted":"lang_origin"}
        lang_target_columns =  {"raw_colums":["lang_target","target_lang","or"], "formatted":"lang_target"}
        source_columns =  {"raw_colums":["source","source_value"], "formatted":"source_columns"}
        source_type_columns =  {"raw_colums":["source_type","type"], "formatted":"source_type"}
        created_at_columns =  {"raw_colums":["created_at","extracted_at"], "formatted":"created_at"}

        # Raise Error if columns not found 
        for dict_cols in [text_origin_columns,text_target_columns, lang_origin_columns, lang_target_columns] :
            df = self.format_column(dict_cols["raw_columns"],dict_cols["formatted"],df, raise_on_not_found=True)

        
        for dict_cols in [source_columns, source_type_columns, created_at_columns]:
            df = self.format_column(dict_cols["raw_columns"],dict_cols["formatted"],df)

        return df 


    def clean_quotechar(self,df:DataFrame)->DataFrame:
        pass 
    def clean_unwanted_characters(self, df:DataFrame)->DataFrame :  
        pass
    