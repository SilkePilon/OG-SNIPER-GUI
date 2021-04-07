import os,sys
import time
from time import sleep

os.system("cls")

def logo():
    print(" _______  _______      _______  _       _________ _______  _______  _______ ")
    time.sleep(0.2)
    print("(  ___  )(  ____ \    (  ____ \( (    /|\__   __/(  ____ )(  ____ \(  ____ )")
    time.sleep(0.2)
    print("| (   ) || (    \/    | (    \/|  \  ( |   ) (   | (    )|| (    \/| (    )|")
    time.sleep(0.2)
    print("| |   | || |          | (_____ |   \ | |   | |   | (____)|| (__    | (____)|")
    time.sleep(0.2)
    print("| |   | || | ____     (_____  )| (\ \) |   | |   |  _____)|  __)   |     __)")
    time.sleep(0.2)
    print("| |   | || | \_  )          ) || | \   |   | |   | (      | (      | (\ (   ")
    time.sleep(0.2)
    print("| (___) || (___) |    /\____) || )  \  |___) (___| )      | (____/\| ) \ \__")
    time.sleep(0.2)
    print("(_______)(_______)    \_______)|/    )_)\_______/|/       (_______/|/   \__/")
    time.sleep(0.2)
    

logo()

name_to_snipe = input("\u001b[34m[\u001b[37mname/account\u001b[34m]\u001b[0m name to snipe : ")
os.system("dir")
print("-")
print("\u001b[34m[\u001b[37mname/account\u001b[34m]\u001b[0m A vaid account file :  \u001b[32myour-mail@test.com:password:question1:question2:question3\u001b[0m ")
account = input("\u001b[34m[\u001b[37mname/account\u001b[34m]\u001b[0m Account file to use : ")

os.system("OGSNIPER_HELPER -n " + name_to_snipe + " -a 3 -p " + account)