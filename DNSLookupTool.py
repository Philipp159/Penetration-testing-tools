import socket

domain = "example.com"

try:
    ip = socket.gethostbyname(domain)
    print(f"{domain} -> {ip}")
except socket.gaierror:
    print("DNS lookup failed")
