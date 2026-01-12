import requests
from datetime import datetime
from pathlib import Path

url = "https://ircc.canada.ca/english/work/iec/selections.xml"

headers = {
    "User-Agent": "Mozilla/5.0 (Python requests)"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

filename = data_folder / f"{datetime.now():%Y-%m-%d}.xml"
with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)