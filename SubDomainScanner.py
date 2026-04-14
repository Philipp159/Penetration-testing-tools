import requests

domain = "example.com"
subdomains = ["www", "mail", "ftp", "dev", "test"]

for sub in subdomains:
    url = f"http://{sub}.{domain}"
    try:
        r = requests.get(url, timeout=2)
        print(f"[OK] {url} ({r.status_code})")
    except:
        pass
