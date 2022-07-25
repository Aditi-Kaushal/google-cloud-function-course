import requests
import json

url = "https://us-central1-bigquerytest-353315.cloudfunctions.net/hello_world"

payload = json.dumps({
    "name": "Aditi",
    "lastname": "Sharma"
})
headers = {
    'Authorization': 'Bearer b11606cbc75c9226a8f4d5190d7ac0f5',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
