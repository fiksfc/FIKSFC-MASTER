# SOC Home Lab - Incident Response

**Analyst:** Fikstella - SOC Tier 1 | Kampala, UG
**Lab Environment:** Linux (Debian) on Chromebook

### 🎯 Objective
Simulate real SOC workflow: Detect SSH Brute-Force attack and auto-respond.

### 📁 Tools Built
1. **soc_log_generator.py** - Generates 100 auth logs with attacker IP `45.33.32.156` doing brute-force
2. **soc_detector.py** - Parses logs, counts failed logins, triggers ALERT if >10 fails
3. **soc_responder.py** - Auto-blocks attacker IP, writes to `blocked_ips.txt`, simulates SOC email alert

### 🚨 Attack Scenario Detected
- Attacker IP: `45.33.32.156`
- Target Users: root, admin, fik
- Pattern: 40+ Failed password attempts in <60 seconds
- Action: BLOCK + ALERT

### ▶️ How to Run
```bash
python3 soc_log_generator.py
python3 soc_detector.py
python3 soc_responder.py

