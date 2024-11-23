from airflow.decorators import task, dag 
from airflow.providers.docker.operators.docker import DockerOperator
from pendulum import datetime
from airflow.models import Variable


@dag(start_date=datetime(2025,1,1), schedule_interval="@monthly", catchup=False,tags=["devia"],)
def hdfs_pipeline():

    HDFS_URL = Variable("HDFS_URL")

    extract_sftp = DockerOperator(
        task_id='extract_sftp',
        image='markreduce/etl:file',
        container_name="extract_sftp",
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
        environment={"HDFS_URL":HDFS_URL,"FILE_PATH":"/translations/file/sftp.csv","SFTP_HOST":Variable("SFTP_HOST"),"SFTP_USERNAME":Variable("SFTP_USERNAME"),"PRIVATE_KEY_PATH":Variable("PRIVATE_KEY_PATH")},
        volumes = ["key:/home/ubuntu/key","known_hosts:/home/ubuntu/.ssh/known_hosts"] # really insecure please note that this is done as it is not the purpose of this code
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
        environment={"HDFS_URL":HDFS_URL,"FILE_PATH":"/translations/web_scrapping.csv"}
    )

    hdfs_transform = DockerOperator(
        task_id='hdfs_transform',
        image='markreduce/etl:hdfs_transform',
        container_name="hdfs_transform",
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
        environment={}
    )

    hdfs_load = DockerOperator(
        task_id='hdfs_load',
        image='markreduce/etl:hdfs_load',
        container_name="hdfs_load",
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
        environment={}
    )    

    hdfs_transform << extract_sftp
    hdfs_transform << extract_cassandra
    hdfs_transform << extract_webscrapping

    hdfs_transform >> hdfs_load

dag = hdfs_pipeline()

