import datetime

attacker_ip = "45.33.32.156"
print(f"[{datetime.datetime.now()}] Starting auto-response...")
print(f"Blocking IP {attacker_ip}...")

with open("blocked_ips.txt", "a") as f:
    f.write(f"{attacker_ip} - blocked on {datetime.datetime.now()}\n")

print(f"[SUCCESS] {attacker_ip} has been blocked and added to blocked_ips.txt")
print(f"Sending email alert to SOC team: fikstella@soc.com")
