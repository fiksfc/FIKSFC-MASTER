from datetime import datetime
import random
import json
import os
import urllib.parse
import webbrowser

MIND_FILE = "fik_mind.json"

def load_mind():
    if os.path.exists(MIND_FILE):
        try:
            with open(MIND_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_to_mind(you_said, assistant_said):
    memories = load_mind()
    memories.append({
        "date": str(datetime.now()),
        "you": you_said,
        "assistant": assistant_said
    })
    with open(MIND_FILE, "w") as f:
        json.dump(memories, f, indent=2)

def show_mind():
    memories = load_mind()
    if not memories:
        print("Mind is empty, bro.")
        return
    for m in memories[-10:]:
        print(f"{m['date']} | You: {m['you']} => {m['assistant']}")

def search_web(query):
    q = urllib.parse.quote(query)
    url = f"https://duckduckgo.com/?q={q}"
    try:
        webbrowser.open(url)
    except:
        pass
    return f"Searching: {query} -> {url}"

slogans = ["strive to observe, build, test and secure"]
quotes = ["Observe, Build, Test and Secure - FIKSFC Master"]

print("FIKSFC MINI ASSISTANT v6.0 - Mind that never forgets + search")
print("Commands: slogan, quote, time, calc 5+8, mind, log text, search topic, bye")

while True:
    q = input("fik> ").strip()
    if not q:
        continue
    if q.lower() == "bye":
        print("Bye bro, mind saved.")
        break
    elif "slogan" in q.lower():
        ans = random.choice(slogans)
        print(ans)
        save_to_mind(q, ans)
    elif "quote" in q.lower():
        ans = random.choice(quotes)
        print(ans)
        save_to_mind(q, ans)
    elif "time" in q.lower():
        ans = str(datetime.now())
        print(ans)
        save_to_mind(q, ans)
    elif q.lower().startswith("calc"):
        try:
            expr = q[4:].strip()
            ans = str(eval(expr))
            print(ans)
            save_to_mind(q, ans)
        except Exception as e:
            print(f"calc error: {e}")
    elif q.lower().startswith("search"):
        topic = q[6:].strip()
        if not topic:
            print("Tell me what to search, e.g., search FIKSFC")
        else:
            ans = search_web(topic)
            print(ans)
            save_to_mind(q, ans)
    elif q.lower().startswith("mind"):
        show_mind()
    elif q.lower().startswith("log"):
        txt = q[3:].strip()
        save_to_mind(txt, "logged")
        print(f"logged: {txt}")
    else:
        ans = f"I got: {q} (saved to my mind)"
        print(ans)
        save_to_mind(q, ans)
