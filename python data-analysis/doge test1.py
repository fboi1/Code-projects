import requests
import json

url = "http://gee:*gee1*@127.0.0.1:22555"
payload = json.dumps({'jsonrpc':'1.0', 'id':'curltest', 'method':'getrawmempool', 'params': [True]})
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response)
print(response.json())