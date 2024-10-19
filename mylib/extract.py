import requests

def extract(
    url="D:/Download/Heroes_3.csv",
    file_path="data/Heroes_3.csv",
):
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path