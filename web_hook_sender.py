import requests as rq
import json

webhook_url="http://127.0.0.1:5000/webhook"

data={"name": " This is just a test for webhook for python"}

rq.post(webhook_url,data=json.dumps(data),headers={'Content-Type':'application/json'})


