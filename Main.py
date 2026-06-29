from Systems.Core import boot
try:
    boot()
except Exception as e:
    print(f"[-] An Error has Accured: {e}")
    print("[!] Please Report this Error at our offical Github Site")
    input("[+] Enter to Close Window.")
    exit()
