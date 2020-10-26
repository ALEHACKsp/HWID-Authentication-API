import requests
import os
from time import sleep

apikey = "QYASDJHASFDUAEFUIYEWRTF87SDAGFHSADFH"

class Authentication:

    def Add(hwid):
        check = requests.get(f'http://127.0.0.1:5000/api/v1/hwid?type=add&hwid={hwid}&apikey={apikey}').text
        if 'success' in check:
            print(f'[\033[32m+\033[39m] Added [\033[91m{hwid}\033[39m] To The Database.')
            sleep(2)
            Main()
        elif 'invalid_apikey' in check:
            print(f'[\033[91m-\033[39m] Invalid API Key\033[91m:\033[39m {apikey}')
            sleep(2)
            Main()

def Main():
    os.system('cls & title [Authentication] By Dropout')
    print(f'''
                                        \033[97m╔═╗╦ ╦╔╦╗╦ ╦╔═╗╔╗╔╔╦╗╦╔═╗╔═╗╔╦╗╦╔═╗╔╗╔\033[39m
                                        \033[37m╠═╣║ ║ ║ ╠═╣║╣ ║║║ ║ ║║  ╠═╣ ║ ║║ ║║║║\033[39m
                                        \033[91m╩ ╩╚═╝ ╩ ╩ ╩╚═╝╝╚╝ ╩ ╩╚═╝╩ ╩ ╩ ╩╚═╝╝╚╝\033[39m
''')
    hwid = input('[\033[91m?\033[39m] HWID\033[91m:\033[39m ')
    Authentication.Add(hwid)

if __name__ == "__main__":
    Main()