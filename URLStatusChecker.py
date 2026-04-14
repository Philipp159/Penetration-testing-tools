import requests

urls = [
    "https://example.com",
    "https://google.com",
]

for url in urls:
    try:
        r = requests.get(url, timeout=3)
        print(f"{url} -> {r.status_code}")
    except:
        print(f"{url} -> DOWN")
