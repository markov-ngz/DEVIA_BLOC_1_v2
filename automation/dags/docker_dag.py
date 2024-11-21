from airflow.decorators import task, dag 
from airflow.providers.docker.operators.docker import DockerOperator
from pendulum import datetime
from airflow.models import Variable

@dag(start_date=datetime(2024,1,1), schedule_interval="@daily", catchup=False,tags=["devia"],)
def docker_dag():
    
    environment = {"API_KEY": Variable.get("API_KEY"),"KAFKA_BOOTSTRAP_SERVER":"broker1:9092","KAFKA_TOPIC":"translations.raw.frpl"}

    extract_api = DockerOperator(
        task_id='extract_api',
        image='markreduce/etl:api',
        container_name="extract_api",
        command='echo "command running in the docker container"',
        docker_url="unix://var/run/docker.sock", # as airflow is run inside docker, the socket must be mounted inside the container so that it can listen to docker daemon 
        network_mode="kafka", # name of container's running network
        environment=environment
    )





dag = docker_dag()