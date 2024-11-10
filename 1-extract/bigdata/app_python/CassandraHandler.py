from cassandra.cluster import Cluster , ResultSet
from cassandra.query import tuple_factory 
from JsonLogger import JsonLogger 

class CassandraHandler(): 

    cluster : Cluster
    
    def __init__(self,ip:str = None, port:int = None, ssl_context = None ) -> None:
        # setting up logger 
        self.logger = JsonLogger()
        self.logger.set_logger(__name__)

        # default ip to localhost & port to 9042 
        port = port if port != None else 9042
        ip = ip if ip != None else '127.0.0.1'

        self.cluster = Cluster([ip],port=port, ssl_context= ssl_context)
    
    def connect(self, keyspace :str )->None:
        try : 
            self.session = self.cluster.connect(keyspace)
        except Exception as e :
            self.logger.error("Could not connect to cluster : {0}".format(str(e)))
            raise e  

    def query(self, query : str )->ResultSet  :
        try : 
            return self.session.execute(query)
        except Exception as e : 
            self.logger.error("Failed to execute the query : {0}".format(str(e)))

    def set_tuple_factory(self)->None:
        """
        Format session to return Row as a tuple object 
        see : https://docs.datastax.com/en/developer/python-driver/3.29/api/cassandra/query/index.html#cassandra.query.tuple_factory 
        """
        self.session.row_factory = tuple_factory

    


