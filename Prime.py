import os
import time
import subprocess

def clear_screen():
    os.system('clear')

def banner():
    print("\033[1;31m" + "☠"*60)
    print("\033[1;36m      [ TARGET HARDWARE LOCALIZATION & RADAR SATELLITE MAP ]")
    print(r"                      .---.        ")
    print(r"              _..---./  X  \.---.._  ")
    print(r"            .'   _./ \  |  / \._   '.")
    print(r"           /   .'     \ | /     '.   \\")
    print(r"          |   /        \|/        \   |")
    print(r"          |  |    Active Grid Map  |  |")
    print(r"          |   \        /|\        /   |")
    print(r"           \   '.     / | \     .'   /")
    print(r"            '.   '._/ \ | / \_.'   .'")
    print(r"              '--..___\_X_/__..--'")
    print(r"                      '---'        ")
    print(r"  ⚡██████╗ ██████╗ ██╗███╗   ███╗███████╗    ██╗   ██╗██╗  ██╗⚡")
    print(r"  ⚡██╔══██╗██╔══██╗██║████╗ ████║██╔════╝    ██║   ██║██║ ██╔╝⚡")
    print(r"  ⚡██████╔╝██████╔╝██║██╔████╔██║█████╗      ██║   ██║█████╔╝ ⚡")
    print(r"  ⚡██╔═══╝ ██╔══██╗██║██║╚██╔╝██║██╔══╝      ╚██╗ ██╔╝██╔═██╗ ⚡")
    print(r"  ⚡██║     ██║  ██║██║██║ ╚═╝ ██║███████╗     ╚████╔╝ ██║  ██╗⚡")
    print(r"  ⚡╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝      ╚═══╝  ╚═╝  ╚═╝⚡")
    print("\033[1;31m" + "☠"*60 + "\033[0m")
    print("\033[1;33m[☠ BROADCAST EXPLOIT // INTRUSION DETECTED // STATUS: COMPROMISED]\033[0m")
    print("\033[1;30m" + " ❌ " * 15 + "\033[0m")

def otg_wipe_tool():
    print("\n\033[1;31m[!] Initializing OTG Destruction Matrix...\033[0m")
    time.sleep(1)
    confirm = input("\033[1;36mExecute hardware wipe sequence? (y/n): \033[0m")
    if confirm.lower() == 'y':
        print("\033[1;32m[✓] Target simulated wipe completed inside secure block!\033[0m")
    else:
        print("\033[1;37m[X] Operation aborted.\033[0m")
    input("\n\033[1;33mPress Enter to return to main panel...\033[0m")

def restart_to_recovery():
    print("\n\033[1;31m[*] Testing ADB Bridge Protocol...\033[0m")
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    if "device" in result.stdout.strip().split('\n')[1:]:
        print("\033[1;32m[+] Target found. Injecting forced reboot exploit...\033[0m")
        os.system("adb reboot recovery")
    else:
        print("\033[1;31m[-] Interface Error: No active device found via ADB connection.\033[0m")
    input("\n\033[1;33mPress Enter to return to main panel...\033[0m")

def show_saved_wifi():
    print("\n\033[1;31m[+] Accessing Protected Hardware Configuration Blocks...\033[0m")
    try:
        output = subprocess.check_output("su -c 'cat /data/misc/wifi/WifiConfigStore.xml'", shell=True, text=True)
        print("\n\033[1;32m[✓] Raw configuration array extracted successfully!\033[0m")
    except:
        print("\033[1;31m[-] System Rejection: Execution requires Root superuser clearance.\033[0m")
    input("\n\033[1;33mPress Enter to return to main panel...\033[0m")

def run_cmd(cmd_string):
    os.system(cmd_string)

def deploy_sqlmap():
    os.system("pkg install python git -y && git clone --depth 1 https://github.com ~/sqlmap && python ~/sqlmap/sqlmap.py --help")

def deploy_wpscan():
    os.system("pkg install ruby -y && gem install wpscan && wpscan --help")

def deploy_metasploit():
    print("\n[+] Downloading Metasploit Framework Base Packages...")
    os.system("pkg install wget curl openssh -y && wget https://github.com && chmod +x metasploit.sh")

def cyber_arsenal_core():
    tool_map = {
        '01': lambda: run_cmd("pkg install nmap -y && clear && nmap"),
        '1': lambda: run_cmd("pkg install nmap -y && clear && nmap"),
        '02': lambda: run_cmd("pkg install whois -y && clear && whois"),
        '2': lambda: run_cmd("pkg install whois -y && clear && whois"),
        '03': lambda: run_cmd("pkg install dnsutils -y && clear && dig -h"),
        '3': lambda: run_cmd("pkg install dnsutils -y && clear && dig -h"),
        '04': lambda: run_cmd("pkg install traceroute -y && clear && traceroute"),
        '4': lambda: run_cmd("pkg install traceroute -y && clear && traceroute"),
        '05': lambda: run_cmd("pkg install netcat -y && clear && nc -h"),
        '5': lambda: run_cmd("pkg install netcat -y && clear && nc -h"),
        '06': lambda: run_cmd("pkg install curl -y && clear && curl --help"),
        '6': lambda: run_cmd("pkg install curl -y && clear && curl --help"),
        '07': lambda: run_cmd("pkg install hydra -y && clear && hydra -h"),
        '7': lambda: run_cmd("pkg install hydra -y && clear && hydra -h"),
        '08': lambda: run_cmd("pkg install john -y && clear && john"),
        '8': lambda: run_cmd("pkg install john -y && clear && john"),
        '09': lambda: run_cmd("pkg install crunch -y && clear && crunch"),
        '9': lambda: run_cmd("pkg install crunch -y && clear && crunch"),
        '10': lambda: run_cmd("pkg install hashcat -y && clear && hashcat --help"),
        '11': lambda: run_cmd("pkg install aircrack-ng -y && clear && aircrack-ng --help"),
        '12': deploy_sqlmap,
        '13': lambda: run_cmd("pkg install nikto -y && clear && nikto -h"),
        '14': lambda: run_cmd("pkg install wget -y && clear && wget --help"),
        '15': lambda: run_cmd("pkg install openssl -y && clear && openssl help"),
        '16': deploy_wpscan,
        '17': lambda: run_cmd("pkg install tcpdump -y && clear && tcpdump --help"),
        '18': lambda: run_cmd("pkg install tshark -y && clear && tshark -h"),
        '19': lambda: run_cmd("pkg install iputils -y && clear && ping -V"),
        '20': lambda: run_cmd("pkg install macchanger -y && clear && macchanger --help"),
        '21': lambda: run_cmd("pkg install proxychains-ng -y && clear && proxychains4"),
        '22': lambda: run_cmd("pkg install openssh -y && clear && ssh -V"),
        '23': lambda: run_cmd("pkg install radare2 -y && clear && r2 -h"),
        '24': lambda: run_cmd("pkg install gdb -y && clear && gdb --help"),
        '25': lambda: run_cmd("pkg install hexedit -y && clear && hexedit --help"),
        '26': lambda: run_cmd("pkg install binutils -y && clear && objdump --help"),
        '27': lambda: run_cmd("pkg install strace -y && clear && strace -h"),
        '28': lambda: run_cmd("pkg install python -y && clear && python --version"),
        '29': lambda: run_cmd("pkg install golang -y && clear && go version"),
        '30': deploy_metasploit
    }
    while True:
        clear_screen()
        banner()
        print("""
\033[1;31m 💀 PRIME CYBER ARSENAL DIRECTORY - 30+ INTENSE UTILITIES 💀\033[0m
\033[1;30m------------------------------------------------------------\033[0m
\033[1;33m [CATEGORY 01: INFORMATION GATHERING & RECON] \033[0m
  01. Nmap Engine     02. Whois Lookup    03. DNSutils (Dig)
  04. Traceroute Core 05. Netcat (nc)     06. Curl Payload Engine
  
\033[1;33m [CATEGORY 02: PASSWORD CRACKING & BRUTEFORCE] \033[0m
  07. Hydra Injector  08. John the Ripper 09. Crunch Wordlist Gen
  10. Hashcat Core    11. Aircrack-ng Package 
  
\033[1;33m [CATEGORY 03: WEB EXPLOITS & VULNERABILITY SCANNERS] \033[0m
  12. SQLMap Engine   13. Nikto Web Scanner 14. Wget Exploiter
  15. OpenSSL Checker 16. WpScan Framework
  
\033[1;33m [CATEGORY 04: NETWORK INTRUSION & PACKET SNIFFERS] \033[0m
  17. Tcpdump Core    18. Wireshark (TShark) 19. IPutils Suite
  20. Macchanger MAC  21. Proxychains Core  22. OpenSSH Tunnel
  
\033[1;33m [CATEGORY 05: REVERSE ENGINEERING & DECOMPILERS] \033[0m
  23. Radare2 Core    24. GDB Debugger     25. Hexedit Array
  26. Binutils Pack   27. Strace Tracker   
  
\033[1;33m [CATEGORY 06: MODERN COMPILERS & EXECUTIONS] \033[0m
  28. Python Payload  29. Golang Engine    30. Metasploit Fetcher
  
\033[1;31m  99. Abort Sub-Console and Return to Main Framework\033[0m
\033[1;30m------------------------------------------------------------\033[0m
        """)
        choice = input("\033[1;31mSelect Weapon Node [01-99]: \033[0m").strip()
        if choice == '99':
            break
        elif choice in tool_map:
            tool_map[choice]()
            input("\n\033[1;33mOperation finished. Press Enter to continue...\033[0m")
        else:
            print("\033[1;31m[-] Invalid Node selection!\033[0m")
            time.sleep(1)

def main_menu():
    main_actions = {
        '1': otg_wipe_tool,
        '2': restart_to_recovery,
        '3': show_saved_wifi,
        '4': cyber_arsenal_core
    }
    while True:
        clear_screen()
        banner()
        print("""
\033[1;30m------------------------------------------------------------\033[0m
\033[1;31m┌────────────────────────┐       ┌────────────────────────┐
│      \033[1;36m[ LOCAL MAP ]\033[1;31m     │       │     \033[1;32m[ PRIME WEAPONS ]\033[1;31m  │
│                        │       │                        │
│    \033[1;35m[Target: Scanning]\033[1;31m  │       │   \033[1;33m1.\033[1;37m OTG Wipe Routine  │
│    \033[1;35m[Grid: Firewalled]\033[1;31m  │       │   \033[1;33m2.\033[1;37m ADB Recovery Hook │
│                        │       │   \033[1;33m3.\033[1;37m WiFi Key Intercept│
│                        │       │   \033[1;33m4.\033[1;32m 30+ Cyber Arsenal │
│                        │       │   \033[1;33m5.\033[1;31m Terminate Session │
└────────────────────────┘       └────────────────────────┘\033[0m
\033[1;30m------------------------------------------------------------\033[0m
\033[1;36m┌──────────────────────────────────────────────────────────┐
│                     \033[1;31m☠ ADMIN DETAILS ☠\033[1;36m                    │
│   \033[1;33m» OPERATOR : \033[1;32mPRIME VK                                  │
│   \033[1;33m» SECTOR   : \033[1;37mDARK WORLD CYBER ARCHITECTURE             │
│   \033[1;33m» SYSTEM   : \033[1;36mTERMUX SECURE ENVIRONMENT                 │
└──────────────────────────────────────────────────────────┘\033[0m
""")
        choice = input("\033[1;31mSelect Main Vector [1-5]: \033[0m").strip()
        if choice == '1':
            otg_wipe_tool()
        elif choice == '2':
            restart_to_recovery()
        elif choice == '3':
            show_saved_wifi()
        elif choice == '4':
            cyber_arsenal_core()
        elif choice == '5':
            print("\n\033[1;31m[!] Terminating session. Stay secure...\033[0m")
            time.sleep(1)
            clear_screen()
            break
        else:
            print("\033[1;31m[-] Invalid Vector selection!\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Execution interrupted by user. Exiting safely...\033[0m")
  
