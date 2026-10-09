# FIKSFC-MASTER - Field Operations Security Fabrication Command
# Build Heavy Career Not Small Toys
import os, sys, time

def banner():
    print("="*50)
    print("  FIKSFC FIELD TOOLKIT - FIKSFC-MASTER")
    print("  Koboko / Kampala - Contact: +254708629256")
    print("="*50)

def scanner():
    print("\n[SCANNER] Scanning...")
    time.sleep(1)
    print("[SCANNER] Done.")

def poster():
    print("\n[POSTER] Creating job sheet...")

def flashing():
    print("\n[FLASHING] Flashing module ready...")

def security():
    print("\n[SECURITY] Running security module...")
    try:
        import fiksfc_security
        fiksfc_security.run()
    except:
        print("[SECURITY] Will add next!")

def main():
    banner()
    while True:
        print("\n1. Scanner\n2. Poster\n3. Flashing\n4. Security\n5. Exit")
        c = input("Select > ")
        if c == "1": scanner()
        elif c == "2": poster()
        elif c == "3": flashing()
        elif c == "4": security()
        elif c == "5": break
        else: print("Invalid")

if __name__ == "__main__":
    main()
