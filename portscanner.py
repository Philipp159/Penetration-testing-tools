import socket

target = "scanme.nmap.org"

for port in range(20, 100):
    s = socket.socket()
    s.settimeout(0.5)

    try:
        s.connect((target, port))
        print("Port offen:", port)
    except:
        pass

    s.close()
