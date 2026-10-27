import random
from datetime import datetime

ips = ["45.33.32.156", "192.168.1.10", "8.8.8.8"]
users = ["admin", "test", "root", "fik"]

with open("auth.log", "w") as f:
    for i in range(100):
        ip = random.choice(ips)
        user = random.choice(users)
        # Make attacker IP fail more
        if ip == "45.33.32.156":
            f.write(f"Oct 25 11:15:{i:02d} kampala-server sshd[1002]: Failed password for {user} from {ip} port 22\n")
        else:
            f.write(f"Oct 25 11:15:{i:02d} kampala-server sshd[1002]: Accepted password for {user} from {ip} port 22\n")
print("[+] auth.log generated with brute-force pattern")
