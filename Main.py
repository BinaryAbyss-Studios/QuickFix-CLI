from Tools.Core import boot
try:
    boot()
except Exception as e:
    print(f"[-] An Error has Accured: {e}")
    input("[+] Enter to Close Window.")
    exit()