""" Simulate database activity to fill the WAL """
import psycopg2
from random import randint
import time
import os

conn = psycopg2.connect(f'dbname={os.getenv("POSTGRES_DB")} user={os.getenv("POSTGRES_USER")} password={os.getenv("POSTGRES_PASSWORD")} port={os.getenv("POSTGRES_PORT")}')

cur = conn.cursor()

a = 1
b = 10000

sol_id = randint(a,b)
ail_id = randint(a,b)
cur.execute(f"INSERT INTO translations (french, polish) VALUES ('{str(sol_id)}','{str(ail_id)}') ")
conn.commit()