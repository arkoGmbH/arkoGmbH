import requests

response = requests.post("https://httpbin.org/post", data={"key": "value"}, headers={"Content-Type": "application/json"})

print(response.json())