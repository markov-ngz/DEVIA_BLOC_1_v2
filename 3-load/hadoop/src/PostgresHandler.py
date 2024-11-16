import psycopg2
from psycopg2.extras import RealDictCursor
from JsonLogger import JsonLogger 


class PostgresHandler():
    """ Postgres Class to do basic operations"""

    def __init__(self, host:str,port:str,database:str,user:str,password:str) -> None:
        """Set basic connection arguments and logger"""
        
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)

        self.host = host 
        self.port = port 
        self.database = database
        self.user = user
        self.password =  password

    def connect(self)->None:
        """
        connect 
        """
        url = f"""postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"""
        try : 
            self.conn = psycopg2.connect(url, cursor_factory = RealDictCursor)
            self.conn.autocommit = True   
        except psycopg2.errors.ConnectionFailure as e :
            self.logger.error(str(e))
            raise e 
        except Exception as e : 
             self.logger.error(str(e))
             raise e
             

    def execute_sql(self, sql:str, returns:bool = True)-> list | None :
        try:
            cursor = self.conn.cursor() 
            cursor.execute(sql) 
            result = cursor.fetchall()
            cursor.close()
        except psycopg2.Error as e : 
            self.logger.error(str(e))
            raise e
        
        if returns : 
            return result  

    def copy_csv(self,table_name:str, sep:str, hquote:str = None, file_path:str=None, buffer = None)->None:
        hquote_expr =  " CSV HEADER QUOTE" + f"'{hquote}'" if  hquote != None else ""
        query = f"""copy {table_name}(text_origin, text_target,languages_id,source_id,extracted_at) FROM stdin WITH DELIMITER '{sep}' {hquote_expr};"""
        try:
            if file_path != None: 
                with open(file_path, 'r', encoding="utf-8") as f:
                        cursor = self.conn.cursor()
                        cursor.copy_expert(
                                query,
                                f
                        )
            elif buffer != None :
                cursor = self.conn.cursor()
                cursor.copy_expert(
                        query,
                        buffer
                )
                self.conn.commit()
            else : 
                raise ValueError("Either buffer or file_path arguments value must be set")
            cursor.close()
        except psycopg2.Error as e:
            self.logger.error(str(e))
            raise e 
        except Exception as e : 
            self.logger.error(str(e))
            raise e 