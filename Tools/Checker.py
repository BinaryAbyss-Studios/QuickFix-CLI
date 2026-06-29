import ctypes
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except AttributeError:
        return False

def reqeust_admin():
    try:
        if not is_admin():
        # Relaunch the script with admin privileges
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, os.path.abspath("Core.py"), None, 1)
            os._exit(0)
    except Exception as e:
        print(f"Failed to gain admin rights: {e}")
        sys.exit(1)


def Main():
    reqeust_admin()
    # Your admin-only code goes here
    print("[+] Running with admin privileges")
    


