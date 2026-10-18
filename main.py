# ———— including system ——————————
import os
import sys
import ctypes
import platform
import threading
#inculding Cmd 
os_name = platform.system()
import subprocess as sp
# ———— including dependencies ——————————
from time import sleep
import webbrowser
if getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))
# —————— Security Block ———————————————————————————————————————————————
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def relaunch_as_admin():
    script_path = sys.argv[0]
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        script_path,
        None,
        1
    )
    sys.exit() # Exit for old instant

def Check__():
    if not is_admin:
        print("[-] This Script Require Admin Preivileges")
        relaunch_as_admin()
    else:
        print("[+] Running with administrator privileges")
# —————— End of the Block ——————————————————————————————————————————————

os.system("title QuickFix v1.2")
print("[+] QuickFix v1.2")
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

print("[+] Preparing Launch")

def Run_Popen(cmd_):
    try:
        result = sp.Popen(
        cmd_,
        stdout=sp.PIPE,
        stderr=sp.STDOUT,
        text=True,
        bufsize=1
        )
        for line in result.stdout:
            print(line, end="")
        
        result.wait()
    except KeyboardInterrupt:
        result.terminate()
        print("[ KeyboardInterrupt ] Process Terminated.")
        sys.exit()

def W_More_Options_funcition():
    print(More_Options)
    while True:
        try:
            More_Options_cmd = input("~> ")
            if More_Options_cmd == "1":
                print("[+] Opening Website.")
                webbrowser.open('https://lobby.binaryabyssstudios.workers.dev/')
            elif More_Options_cmd == "2":
                print("[+] Showing Source Code.")
                webbrowser.open('https://github.com/BinaryAbyss-Studios/QuickFix-CLI')
            elif More_Options_cmd == "3":
                print("[!] Exiting from More Options.")
                return
                break
        except KeyboardInterrupt:
            print("[ KeyboardInterrupt ] Process Terminated.")
            sys.exit()
        except Exception as e:
            print(f"[ UNHANDLED EXCEPTION ] {e}")
            
def W_Menu():
    print(Service)
    choice = None
    while True:   
        choice = input("~> ")
        match choice:
            case "1":
                print("[+] Manual Decected..")
                W_Manual()
            case "2":
                print("[+] Automatic Decected..")
                W_Automatic()
                break
            case "3":
                print(More_Options)
                while True:
                    More_Options_cmd = input("~> ")
                    if More_Options_cmd == "1":
                        print("[+] Opening Website.")
                        try:
                            webbrowser.open('https://lobby.binaryabyssstudios.workers.dev/')
                        except Exception as ex:
                            print(f"[-] an Error has Accured: {ex}" )
                    elif More_Options_cmd == "2":
                        print("[+] Showing Source Code.")
                        try:
                            webbrowser.open('https://github.com/BinaryAbyss-Studios/QuickFix-CLI')
                        except Exception as ex:
                            print(f"[-] an Error has Accured: {ex}" )
                    elif More_Options_cmd == "3":
                        print("[!] Exiting from More Options.")
                        print(Service)
                        break
            case "4":
                print("[</>] Exiting Program")
                sleep(0.5)
                sys.exit()
            case _:   
                print("[-] Invaild Input.")
            



def W_Manual():
    print("[+] Manual Boot Starting.")
    print(logo)
    print(Manual_Service , "\n")
    while True:
        try:
            Terminal_choice = input("~> ")
            match Terminal_choice:
                case "1":
                    Run_Popen(["sfc", "/scannow"])
                case "2":    
                    Run_Popen(["DISM", "/Online", "/Cleanup-Image", "/RestoreHealth"])
                case "3":
                    Run_Popen(["DISM", "/Online", "/Cleanup-Image", "/ScanHealth"])
                case "4": 
                    Run_Popen(["DISM", "/Online", "/Cleanup-Image", "/StartComponentCleanup"])
                case "5":
                    Run_Popen(["DISM", "/Cleanup-MountPoints"])
                case "6":
                    os.system("echo Y|chkdsk /f /r C:")
                    print("[+] Command Executed Succesfully.")
                case "7":
                    W_More_Options_funcition()
                    return
                case "8":
                    print("[+] Exiting Manual Mode.")
                    W_Menu()
                    return
                case _:
                    print("[-] Invaild Input")
        except KeyboardInterrupt:
            print("[ Keyboard Interrupt ] Exiting")
            sys.exit()
        except Exception as e:
            print(f"[ UNHANDELD EXCEPTION ] {e}")
    
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
            Run_Popen(checkcmd)
        print("[+] Running Repair + Optimization Please wait..")
        for cmd in commands:
            Run_Popen(cmd)
        print("[!] Do you want to run the CHKDSK (full disk Checkup)")
        choice_chkdsk = input("y/N: ").strip().lower()
        letter_check = "y"
        if letter_check in choice_chkdsk:
            print("[+] Scheduling CHKDSK...")
            result = os.system("echo Y|chkdsk /f /r C:")
            if result == 0:
                print("[+] Finished Successfully")
            else:
                print("[-] CHKDSK finished with errors.")
        else:
            print("[-] Operation Disabled")
            pass
        print("enter 1 to close program , enter 2 to relaunch program , enter 3 to restart Computer (Recommended)")
        while True:
            choice = input("~> ")
            if choice == "1":
                sys.exit()
            elif choice == "2":
                relaunch_as_admin()
            elif choice == "3":
                os.system("shutdown /r /t 0")
                return
            else:
                print("[-] Invaild Input")
    except KeyboardInterrupt:
        print("[ KeyboardInterrupt ] Exiting.")
        return
    except Exception as ex:
            print(f"[-] an Error Accured: {ex}")
            print("[-] Please try again")
            input("[!] Enter Anything to Exit.")
            return


def main():
    print(f"[+] Running on {os_name}")
    if os_name != "Windows":
        print("[!] OS is not supported.")
        sys.exit()
    Check__()
    W_Menu()

if __name__ == "__main__":
    main()