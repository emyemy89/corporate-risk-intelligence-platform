import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

headers = {
    "User-Agent": f"FinancialRiskProject {os.getenv('API_CONTACT_EMAIL')}"
}

url = (
    "https://data.sec.gov/api/xbrl/companyfacts/"
    "CIK0000789019.json" # Microsoft
)
response = requests.get(url, headers=headers, timeout=30)
response.raise_for_status()

data_json = response.json()
print(data["entityName"])
print(data["facts"].keys())

