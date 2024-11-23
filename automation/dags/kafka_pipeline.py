from airflow.decorators import task, dag 
from airflow.providers.docker.operators.docker import DockerOperator
from pendulum import datetime
from airflow.models import Variable

@dag(start_date=datetime(2024,1,1), schedule_interval="@daily", catchup=False,tags=["devia"],)
def kafka_pipeline():
    
    environment = {"API_KEY": Variable.get("API_KEY"),"KAFKA_BOOTSTRAP_SERVER":"broker1:9092","KAFKA_TOPIC":"translations.raw.frpl"}

    extract_api = DockerOperator(
        task_id='extract_api',
        image='markreduce/etl:api',
        container_name="extract_api",
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
        environment=environment
    )
    cdc_format = DockerOperator(
        task_id='cdc_format',
        image='markreduce/etl:kafkacdc',
        container_name="kafka_cdc_format",
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
    )
    kafka_transform = DockerOperator(
        task_id='kafka_transform',
        image='markreduce/etl:kafkatransform',
        container_name="kafka_transform",
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
    )

    kafka_load = DockerOperator(
        task_id='kafka_load',
        image='markreduce/etl:kafkaload',
        container_name="kafka_load",
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
    )

    kafka_transform << cdc_format
    kafka_transform << extract_api

    kafka_transform >> kafka_load


kafka_pipeline()