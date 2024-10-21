""" Simulate database activity to fill the WAL """
import psycopg2
from random import randint
import time
import os

conn = psycopg2.connect(f"dbname={os.getenv("POSTGRES_DB")} user={os.getenv("POSTGRES_USER")} password={os.getenv("POSTGRES_PASSWORD")}")

cur = conn.cursor()

a = 1
b = 10000
while True:
    sol_id = randint(a,b)
    ail_id = randint(a,b)
    cur.execute(f"INSERT INTO ref_sol_ail (sol_id, ail_id) VALUES ({str(sol_id)},{str(ail_id)}) ")
    conn.commit()
    cur.execute(f"DELETE FROM ref_sol_ail  WHERE sol_id = {str(sol_id)} AND ail_id = {str(ail_id)} ")
    conn.commit()
    time.sleep(15)