import os

network = "192.168.1."

for i in range(1, 255):
    ip = network + str(i)
    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null")
    
    if response == 0:
        print(f"[LIVE] {ip}")
