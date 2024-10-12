FROM ubuntu:latest

RUN apt update -y

RUN apt install python3 python3-pip openssh-client -y

USER ubuntu 

RUN mkdir /home/ubuntu/.ssh

COPY ./src /home/ubuntu/
COPY ./requirements.txt /home/ubuntu/requirements.txt
COPY ./entrypoint.sh /

RUN pip install -r /home/ubuntu/requirements.txt --break-system-packages

WORKDIR /home/ubuntu

ENTRYPOINT ["sh","/entrypoint.sh"]