import os
from databricks import sql
from dotenv import load_dotenv

complex_query = """
SELECT
    h1.Heroes,
    h1.Hero_Score,
    h1.Race,
    AVG(h1.Hero_Score) AS Average_Hero_Score,
    AVG(h1.Race_Score) AS Average_Race_Score
FROM default.hd_heroes AS h1
JOIN default.hd_heroes AS h2
ON h1.Heroes = h2.Heroes
GROUP BY h1.Race, h1.Heroes, h1.Hero_Score
ORDER BY h1.Hero_Score DESC;
"""

def query():
    load_dotenv()
    with sql.connect(server_hostname=os.getenv("SERVER_HOSTNAME"),
                     http_path=os.getenv("HTTP_PATH"),
                     access_token=os.getenv("DATABRICKS_KEY")) as connection:
        with connection.cursor() as cursor:
            cursor.execute(complex_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.close()
            connection.close()

    return "Query Success"

if __name__ == "__main__":
    query()
