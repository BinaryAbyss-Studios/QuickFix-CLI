# including system
import os
import sys
import platform
#inculding Cmd 
import subprocess as sp
try:
    from Tools import Checker as CK  # when run from Main.py
except ModuleNotFoundError:
    import Checker as CK  # when run directly
#including depencites
import time
import webbrowser
import random
if getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))

#---- Core.py v1.1 ----#
#- Open Source Code Changeable Customizeable No bloat.
#- have fun.

os.system("title QuickFix v1.1")
os_name = platform.system()
Service = "[1] Manual , [2] Automatic , [3] More Options , [4] Exit Program "
Manual_Service = """
[1] sfc scan ,         [2] restore health ,                 [3] Scan health , 
[4] component cleaup , [5] Clean Mount points + curroption , [6] Full Disk Scan, 
[7] More Options ,     [8] Exit
"""
More_Options = """[1] Visit Website , [2] Show Source Code , [3] Exit"""
logo = """
    ██████    █████  █████ █████   █████████  █████   ████    ███████████ █████ █████ █████
  ███▒▒▒▒███ ▒▒███  ▒▒███ ▒▒███   ███▒▒▒▒▒███▒▒███   ███▒    ▒▒███▒▒▒▒▒▒█▒▒███ ▒▒███ ▒▒███ 
 ███    ▒▒███ ▒███   ▒███  ▒███  ███     ▒▒▒  ▒███  ███       ▒███   █ ▒  ▒███  ▒▒███ ███  
▒███     ▒███ ▒███   ▒███  ▒███ ▒███          ▒███████        ▒███████    ▒███   ▒▒█████   
▒███   ██▒███ ▒███   ▒███  ▒███ ▒███          ▒███▒▒███       ▒███▒▒▒█    ▒███    ███▒███  
▒▒███ ▒▒████  ▒███   ▒███  ▒███ ▒▒███     ███ ▒███ ▒▒███      ▒███  ▒     ▒███   ███ ▒▒███ 
 ▒▒▒██████▒██ ▒▒████████   █████ ▒▒█████████  █████ ▒▒████    █████       █████ █████ █████
   ▒▒▒▒▒▒ ▒▒   ▒▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒   ▒▒▒▒    ▒▒▒▒▒       ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒ 
                                                                                           
                                                                                           
                                                                                           """

# Custom Loading Animation for old end devices and stability.
def W_Launching():
    CK.Main()
    print("[+] Preparing Launch.")
    rand = random.randint(10, 70)

    frames = ["/", "-", "\\", "|"]
    for i in range(rand):  # how many spins
        print(f"\rloading.. {frames[i % 4]}", end="", flush=True)
        time.sleep(0.1)
    
    print("\r[+] Done!               \n")
    W_Menu()

def W_More_Options_funcition():
    print(More_Options)
    while True:
        try:
            More_Options_cmd = input("~> ")
        except KeyboardInterrupt:
            print("\n[!] Exiting Program. Goodbye")
            input("[+] Enter to Close Window \n")
            sys.exit()
        if More_Options_cmd == "1":
            print("[+] Opening Website.")
            try:
                webbrowser.open('https://binaryabyssstudios.github.io/')
            except Exception as ex:
                print(f"[-] an Error has Accured: {ex}" )
        elif More_Options_cmd == "2":
            print("[+] Showing Source Code.")
            try:
                webbrowser.open('https://github.com/BinaryAbyssStudios/quickfix')
            except Exception as ex:
                print(f"[-] an Error has Accured: {ex}" )
        elif More_Options_cmd == "3":
            print("[!] Exiting from More Options.")
            W_Menu()
            break
            
# a funcition starts with W means its meant for Windows.
def W_Menu():
    print(Service)
    choice = None
    while True:   
        try:
            choice = input("~> ")
        except KeyboardInterrupt:
            print("\n[!] Exiting Program. Goodbye")
            input("[+] Enter to Close Window\n ")
            sys.exit()
        if choice == "1":
            print("[+] Manual Decected..")
            W_Manual()
        elif choice == "2":
            print("[+] Automatic Decected..")
            W_Automatic()
            break
        elif choice =="3":
            print(More_Options)
            while True:
                More_Options_cmd = input("~> ")
                if More_Options_cmd == "1":
                    print("[+] Opening Website.")
                    try:
                        webbrowser.open('https://binaryabyssstudios.github.io/')
                    except Exception as ex:
                        print(f"[-] an Error has Accured: {ex}" )
                elif More_Options_cmd == "2":
                    print("[+] Showing Source Code.")
                    try:
                        webbrowser.open('https://github.com/BinaryAbyssStudios/quickfix')
                    except Exception as ex:
                        print(f"[-] an Error has Accured: {ex}" )
                elif More_Options_cmd == "3":
                    print("[!] Exiting from More Options.")
                    print(Service)
                    break
        elif choice == "4":
            print("[</>] Exiting Program")
            time.sleep(0.5)
            sys.exit()
        else:   
            print("[-] Invaild Input.")
            



def W_Manual():
    print("[+] Manual Boot Starting.")
    print(logo)
    print(Manual_Service , "\n")
    while True:
        try:
            Terminal_choice = input("~> ")
        except KeyboardInterrupt:
            print("\n[!] Exiting Program. Goodbye")
            input("[+] Enter to Close Window \n")
            sys.exit()
        if Terminal_choice == "1":
            try:    
                sfc = sp.run('sfc /scannow', shell=True)
            except Exception as ex:
                print(f"[-] An Error has Accured: {ex}")
        elif Terminal_choice == "2":
            try:    
                DISM = sp.run('DISM /Online /Cleanup-Image /RestoreHealth', shell=True)
            except Exception as ex:
                print(f"[-] An Error has Accured: {ex}")
        elif Terminal_choice == "3":
            try:    
                DISM = sp.run('DISM /Online /Cleanup-Image /ScanHealth', shell=True)
            except Exception as ex:
                print(f"[-] An Error has Accured: {ex}")
        elif Terminal_choice == "4":
            try:    
                DISM = sp.run('DISM /Online /Cleanup-Image /StartComponentCleanup', shell=True)
            except Exception as ex:
                print(f"[-] An Error has Accured: {ex}")
        elif Terminal_choice == "5":
            try:    
                DISM = sp.run('DISM /Cleanup-MountPoints', shell=True)
            except Exception as ex:
                print(f"[-] An Error has Accured: {ex}")
        elif Terminal_choice == "6":
            os.system("echo Y|chkdsk /f /r C:")
            print("[+] Command Executed Succesfully.")
        elif Terminal_choice == "7":
            W_More_Options_funcition()
            return
        elif Terminal_choice == "8":
            print("[+] Exiting Manual Mode.")
            W_Menu()
            return
    
def W_Automatic():
    commands = [
        "sfc /scannow",
        "DISM /Online /Cleanup-Image /RestoreHealth",
        "DISM /Online /Cleanup-Image /StartComponentCleanup",
        "DISM /Cleanup-MountPoints",
    ]
    checking_health = [
        "DISM /Online /Cleanup-Image /CheckHealth",
        "DISM /Online /Cleanup-Image /ScanHealth"
    ]

    print("[+] Automatic Boot Started.")
    print(logo)
    try:
        print("[+] Checking Health")
        for checkcmd in checking_health:
            result_health = sp.run(checkcmd , shell=True)
        print("[+] Running Repair + Optimization Please wait..")
        for cmd in commands:
            result = sp.run(cmd, shell=True)
        print("[+] Scheduling CHKDSK...")
        os.system("echo Y|chkdsk /f /r C:")
        print("[+] Finished Successfully")
        print("enter 1 to close program , enter 2 to relaunch program , enter 3 to restart Computer (Recommended)")
        while True:
            choice = input("~> ")
            if choice == "1":
                sys.exit()
            elif choice == "2":
                W_Launching()
            elif choice == "3":
                os.system("shutdown /r /t 0")
                return
            else:
                print("[-] Invaild Input")
    except Exception as ex:
            print(f"[-] an Error Accured: {ex}")
            print("[-] Please try again")
            input("[!] Enter Anything to Exit.")
            return
            
def boot():
    if os_name == "Windows":
        print(f"[+] Running on {os_name}")
        W_Launching()
    elif os_name == "Linux":
        print(f"[+] Running on {os_name}")
        print("[!] os Not Supported yet")
        time.sleep(10)
    elif os_name == "Darwin":
        print(f"[+] Running on {os_name}")
        print("[!] os Not Supported yet")
        time.sleep(10)
    else:
        print("[!] os Not Suppported yet")
        time.sleep(10)

boot()