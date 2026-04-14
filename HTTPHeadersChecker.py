import requests

url = "https://example.com"

r = requests.get(url)

print("Headers:")
for k, v in r.headers.items():
    print(f"{k}: {v}")
