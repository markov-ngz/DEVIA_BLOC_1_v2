from airflow.decorators import task, dag 
from airflow.providers.docker.operators.docker import DockerOperator
from pendulum import datetime
from airflow.models import Variable
from docker.types import Mount

@dag(start_date=datetime(2024,1,1), schedule_interval="@monthly", catchup=False,tags=["devia"],)
def hdfs_pipeline():

    HDFS_URL = Variable.get("HDFS_URL")

    extract_sftp = DockerOperator(
        task_id='extract_sftp',
        image='markreduce/etl:file',
        container_name="extract_sftp",
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
        environment={"HDFS_URL":HDFS_URL,"FILE_PATH":"/translations/sftp/sftp.csv","REMOTE_FILE":Variable.get("REMOTE_FILE"),"SFTP_HOST":Variable.get("SFTP_HOST"),"SFTP_USERNAME":Variable.get("SFTP_USERNAME"),"PRIVATE_KEY_PATH":Variable.get("PRIVATE_KEY_PATH")},
        mounts = [Mount(source="sftp_key",target="/home/ubuntu",read_only=True)] # really insecure please note that this is done as it is not the purpose of this code
    )

    extract_cassandra = DockerOperator(
        task_id='extract_cassandra',
        image='markreduce/etl:bigdata',
        container_name="extract_cassandra",
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
        environment={"HDFS_URL":HDFS_URL,"FILE_PATH":"/translations/cassandra/cassandra.csv","CASSANDRA_IP":"node-1","CASSANDRA_KEYSPACE":"translations","CASSANDRA_TABLE":"pl_fr"}
    )

    extract_webscrapping = DockerOperator(
        task_id='extract_webscrapping',
        image='markreduce/etl:webscrapping',
        container_name="extract_webscrapping",
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
        environment={"HDFS_URL":HDFS_URL,"FILE_PATH":"/translations/web_scrapping/web_scrapping.csv"}
    )

    hdfs_transform = DockerOperator(
        task_id='hdfs_transform',
        image='markreduce/etl:hadooptransform',
        container_name="hdfs_transform",
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
        environment={"HDFS_URL":HDFS_URL,"HDFS_FOLDER":"/translations/output/","HDFS_SOURCES":Variable.get("HDFS_SOURCES")}
    )

    hdfs_load = DockerOperator(
        task_id='hdfs_load',
        image='markreduce/etl:hadoopload',
        container_name="hdfs_load",
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
        environment={"DB_HOST":"target_db","DB_PORT":"5432","DB_PASSWORD":"raditz","DB_NAME":"TARGET_DB","DB_USERNAME":"TARGET_USER","HDFS_URL":HDFS_URL,"HDFS_FOLDER":"/translations/output"}
    )    

    hdfs_transform << extract_sftp
    hdfs_transform << extract_cassandra
    hdfs_transform << extract_webscrapping

    hdfs_transform >> hdfs_load

hdfs_pipeline()

