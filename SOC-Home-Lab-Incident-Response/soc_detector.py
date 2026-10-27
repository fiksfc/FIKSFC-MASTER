from collections import Counter

print("--- SOC Analysis ---")
with open("auth.log") as f:
    lines = f.readlines()

failed = []
for line in lines:
    if "Failed password" in line:
        ip = line.split("from")[1].split()[0]
        failed.append(ip)

count = Counter(failed)
for ip, c in count.items():
    print(f"IP {ip} failed {c} times")
    if c > 10:
        print(f"🚨 ALERT! Brute-Force Detected from {ip}!")
        print(f"Recommendation: BLOCK IP {ip} immediately")
        print("Evidence:")
        for l in lines:
            if ip in l and "Failed" in l:
                print(f" - {l.strip()}")
