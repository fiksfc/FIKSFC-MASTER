from datetime import date, time, datetime
import random, json, os

def save_to_mind(you_said, assistant_said):
    file = "cyber_project/memory.json"
    if not os.path.exists("cyber_project"):
        os.makedirs("cyber_project")
    memories = []
    if os.path.exists(file):
        try:
            memories = json.loads(open(file).read())
        except:
            memories = []
    memories.append({"date": str(datetime.now()), "you": you_said, "me": assistant_said})
    open(file, "w").write(json.dumps(memories, indent=2))

def show_mind(keyword=""):
    file = "cyber_project/memory.json"
    if not os.path.exists(file):
        print("Mind is still empty.")
        return
    memories = json.loads(open(file).read())
    if keyword == "":
        for m in memories[-5:]:
            print(f"{m['date']} - You: {m['you']} | Me: {m['me']}")
    else:
        for m in memories:
            if keyword.lower() in m["you"].lower() or keyword.lower() in m["me"].lower():
                print(f"{m['date']} - You: {m['you']} | Me: {m['me']}")

slogans = ["strive to observe, build, test and secure"]
quotes = ["test - nothing is unbreakable", "learn daily"]

print("FIKSFC MINI ASSISTANT v5.0 - Mind that never forgets")
print("Commands: slogan, quote, time, calc 5+8, mind, mind keyword, log text, bye")

while True:
    q = input("fik> ").strip()
    if not q:
        continue

    if q.lower() == "slogan":
        print(slogans[0])
        save_to_mind(q, slogans[0])

    elif q.lower() == "quote":
        ans = random.choice(quotes)
        print(ans)
        save_to_mind(q, ans)

    elif q.lower() == "time":
        ans = f"Time now: {datetime.now()}"
        print(ans)
        save_to_mind(q, ans)

    elif q.lower().startswith("calc"):
        try:
            expr = q[5:].strip().lower()
            if not expr:
                print("Usage: calc 5+8-2 or calc 300*4")
            else:
                expr = expr.replace("x", "*")
                result = eval(expr)
                ans = f"Result:{result}"
                print(ans)
                save_to_mind(q, ans)
        except Exception as e:
            print(f"Calc error: {e}")

    elif q.lower() == "mind":
        show_mind()

    elif q.lower().startswith("mind "):
        show_mind(q[5:])

    elif q.lower().startswith("log "):
        text = q[4:]
        open("cyber_project/DAILY_LOG.txt", "a").write(f"{datetime.now()} - {text}\n")
        print("Logged.")
        save_to_mind(q, "Logged to DAILY_LOG.txt")

    elif q.lower() in ["bye", "exit", "quit"]:
        print("Exiting - strive to observe, build, test and secure.")
        break

    else:
        ans = f"Got it: {q} - saved to my mind"
        print(ans)
        save_to_mind(q, ans)
