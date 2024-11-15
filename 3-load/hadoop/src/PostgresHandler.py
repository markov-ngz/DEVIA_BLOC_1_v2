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
             

    def execute_sql(self, sql:str)-> None :
        try:
            cursor = self.conn.cursor() 
            cursor.execute(sql) 
            cursor.close()
        except psycopg2.Error as e : 
            self.logger.error(str(e))
            raise e 
         
    def copy_local_csv(self, file_path:str,table_name:str, sep:str, hquote:str)->None:
        query = f"""copy {table_name} FROM stdin WITH DELIMITER '{sep}' CSV HEADER QUOTE '{hquote}';"""
        try:
            with open(file_path, 'r', encoding="utf-8") as f:
                    cursor = self.conn.cursor()
                    self.cursor.copy_expert(
                            query,
                            f
                    )
                    cursor.close()
        except psycopg2.Error as e:
            self.logger.error(str(e))
            raise e 
        except Exception as e : 
            self.logger.error(str(e))
            raise e 