# Using Python to get JSON from http and save as json file
# by seaniwei

import requests
import json
data = requests.get(url="https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0002-001?Authorization=rdec-key-123-45678-011121314&format=JSON")
with open("music.json","w",encoding="utf-8") as myFile:
    json.dump(data.json(), myFile,ensure_ascii=False)
myFile.close()
