import requests, json

URL_WORDS = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230202T193237Z&X-Amz-Expires=86400&X-Amz-Signature=4bdcad07536f2a029e3ea595b265fc98a67c2ba96d2e5dac3092eb700e1f7b13&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject"

req = requests.get(URL_WORDS)  # json записывается в переменную

data = req.json()
print(req.text)
#raw_json = json.dumps(data)
#print(raw_json)
#data = json.dumps(data)
#raw_json = json.loads(req.text)

with open('data.json', 'w') as f:  # 
  f.write(req.text)