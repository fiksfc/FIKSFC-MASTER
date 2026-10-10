print("=== FIKSFC MINI v4.1 ===")
import datetime, random
name=input("Your name? ").strip() or "Fik"
print(f"Welcome {name}! slogan: strive to observe, build, test and secure.")
slogan="strive to observe, build, test and secure."
quotes=[slogan,"observe first","build - koboko to world","test - nothing is unbreakable","secure - fix don't break"]
while True:
    q=input(f"\n{name}> ").strip()
    if q.lower() in ["bye","exit","back"]: break
    if q.lower()=="slogan": print(f"\n*** {slogan} ***")
    elif q.lower()=="quote": print(random.choice(quotes))
    elif q.lower().startswith("log "): open("cyber_project/DAILY_LOG.txt","a").write(f"{q[4:]}\n"); print("Logged!")
    else: print(f"Got it: {q}")
