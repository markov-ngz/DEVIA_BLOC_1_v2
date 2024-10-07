FROM python:3.11-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

RUN mkdir logs

ENV PATH="/usr/src/app/utils/chromedriver:$PATH"
RUN echo "export PATH=$PATH" >> /etc/profile

CMD ["sleep","10000"]