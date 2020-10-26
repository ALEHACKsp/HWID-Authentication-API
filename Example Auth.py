import requests
import subprocess
import os
from time import sleep

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

class Authentication:

    def Check(hwid):
        check = requests.get(f'http://127.0.0.1:5000/api/v1/hwid?type=check&hwid={hwid}').text
        if 'success' in check:
            print(f'[\033[32m+\033[39m] Success Welcome Back, {os.getenv("UserName")}!')
            sleep(2)
            Program()
        elif 'invalid_hwid' in check:
            print(f'[\033[91m-\033[39m] Invalid HWID\033[91m:\033[39m {hwid}')
            sleep(5)
            Main()

def Program():
    os.system('cls')
    input('Hello World')

def Main():
    os.system('cls & title [Authentication] By Dropout')
    print(f'''
                                        \033[97m╔═╗╦ ╦╔╦╗╦ ╦╔═╗╔╗╔╔╦╗╦╔═╗╔═╗╔╦╗╦╔═╗╔╗╔\033[39m
                                        \033[37m╠═╣║ ║ ║ ╠═╣║╣ ║║║ ║ ║║  ╠═╣ ║ ║║ ║║║║\033[39m
                                        \033[91m╩ ╩╚═╝ ╩ ╩ ╩╚═╝╝╚╝ ╩ ╩╚═╝╩ ╩ ╩ ╩╚═╝╝╚╝\033[39m

[\033[91mDISCORD\033[39m] 766589097161654272
[\033[91mWEBSITE\033[39m] google.com
''')
    Authentication.Check(hwid)

if __name__ == "__main__":
    Main()