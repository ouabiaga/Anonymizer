from faker import Faker
from selenium import webdriver
from getpass import getpass
import platform
import subprocess
import os
fake = Faker()
def text():
    print(r"""
 ____  _      ____  _     ___  _ _      _  ____  _____ ____ 
/  _ \/ \  /|/  _ \/ \  /|\  \/// \__/|/ \/_   \/  __//  __\
| / \|| |\ ||| / \|| |\ || \  / | |\/||| | /   /|  \  |  \/|
| |-||| | \||| \_/|| | \|| / /  | |  ||| |/   /_|  /_ |    /
\_/ \|\_/  \|\____/\_/  \|/_/   \_/  \|\_/\____/\____\\_/\_\
                                                            """)
    print("Powered Faker and Selenium")
    print("Dont Use illegal activities")
    print("writed By serpten")

def InputText():
    print(r"""
         [1] fake Name And Surname
         [2] fake EMail
         [3] fake contry
         [4] fake address
         [5] Google doesn't record search history 
          (your search history isn't saved, but websites can still access data like your IP address).
         [6] Firefox doesn't record search history 
          (your search history isn't saved, but websites can still access data like your IP address).
         [7] Open Vpn (first try normal and second you can try the root)
          """)
try:
    while True:
        text()
        InputText()
        i =int(input("Give me Number : "))
        if i == 1:
            print("Name For male ",fake.name_male())
            print("Name For female ",fake.name_female())
        elif i == 2:
            print(fake.free_email())
        elif i==3:
            print(fake.country())
        elif i==4:
            print(fake.address())
        elif i==5:
            driver=webdriver.Chrome()
            url="https://www.google.com/"
            driver.get(url)
            x=input("if you want close the chrome input enter ")
            driver.quit()
            
        elif i==6:
            driver=webdriver.Firefox()
            url="https://www.google.com/"
            driver.get(url)
            x=input("if you want close the firefox input enter ")
            driver.quit()
        elif i==7:
            vpnname = input("Enter VPN name: ")
            user = input("Enter username: ")
            passw =getpass("Enter password")
            system = platform.system()
            try:
                    if system == "Windows":
                        try:
                            cmd_command = f'rasdial "{vpnname}" {user} {passw}'
                            result = subprocess.run(cmd_command, shell=True, check=True, capture_output=True, text=True)
                            print("Connected to VPN")
                        except subprocess.CalledProcessError as e:
                            print(f"Connect Error: {e.output}")
                    elif system == "Linux":
                        subprocess.run(["sudo", "openvpn", "--config", f"/etc/openvpn/{vpnname}.ovpn"])
                    elif system == "Darwin":  # macOS
                        subprocess.run(["networksetup", "-connectpppoeservice", vpnname])
                    else:
                        print("Unsupported OS:", system)
            except Exception as e:
                print("VPN connection failed:", e)
        elif i== 0:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            break
        else:
            print("invalid process")
except Exception as e:
    print("error ",e)
