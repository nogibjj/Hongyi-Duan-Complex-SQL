import requests

def extract(
    url="https://raw.githubusercontent.com/nogibjj/Hongyi-Duan-Complex-SQL/main/Heroes_3.csv",
    file_path="data/Heroes_3.csv",
):
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
