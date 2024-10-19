import csv
import os
from dotenv import load_dotenv
from databricks import sql

def load(dataset='data/Heroes_3.csv'):
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)
    load_dotenv()
    with sql.connect(server_hostname = os.getenv("SERVER_HOSTNAME"),
                    http_path       = os.getenv("HTTP_PATH"),
                    access_token    = os.getenv("DATABRICKS_KEY")) as connection:
        
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS hd_heroes
                           (Heroes STRING, Skill_1 STRING, Skill_2 STRING,
                           Race STRING, Hero_Score FLOAT, Race_Score FLOAT);
                           """)
            string_sql = "INSERT INTO hd_heroes VAlUES"
            for i in payload:
                print(i)
                string_sql += "\n" + str(tuple(i)) + ","
            string_sql = string_sql[:-1] + ";"
            cursor.execute(string_sql)
            cursor.close()
            connection.close()

if __name__ == "__main__":
    load()