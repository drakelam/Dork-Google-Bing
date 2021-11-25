import webbrowser, os, time, sys
import colorama
from colorama import init, Fore, Style
import ctypes
def logo():
    if os.name == "nt":
        ctypes.windll.kernel32.SetConsoleTitleW('DorkSea v1.0 | Coded by: Drake Lam | DrakeLam.Com')
        os.system('cls')    
    else:
        os.system('clear')
    print(Fore.LIGHTBLUE_EX + """
 
██████╗ ██████╗  █████╗ ██╗  ██╗███████╗    ██╗      █████╗ ███╗   ███╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝    ██║     ██╔══██╗████╗ ████║
██║  ██║██████╔╝███████║█████╔╝ █████╗      ██║     ███████║██╔████╔██║
██║  ██║██╔══██╗██╔══██║██╔═██╗ ██╔══╝      ██║     ██╔══██║██║╚██╔╝██║
██████╔╝██║  ██║██║  ██║██║  ██╗███████╗    ███████╗██║  ██║██║ ╚═╝ ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                

""")
    print(Fore.WHITE + "                       Made by:" + Fore.RED + " Drake Lam" + Fore.GREEN + " | V1.0")
    print(Style.RESET_ALL)
                                                                                                                                
def engine():
    logo()
    print("""
    [1] Bing
    [2] Google
    """)
    x = input('Select: ')
    if x == '1':
        bing()
    elif x == '2':
        google()
    else:
        engine()



def google():
    anon = 'anonfile.com+'
    drive = 'drive.google.com+'
    crax = 'crax.pro+'
    past = 'pastebin.com+'
    site = 'site:'
    logo()
    print("""
    [1] Anonfile
    [2] Google Drive
    [3] Crax Pro
    [4] Pastebin
    [<] Back
    """)
    mode = input('Select: ')
    if mode == '1':
        logo()        
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+site+anon+key)
        google()
    elif mode == '2':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+site+drive+key)
        google()
    elif mode == '3':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+site+crax+key)
        google()
    elif mode == '4':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+site+past+key)
        google()
    elif mode == '<':
        engine()
    else:
        google()
    

def bing():
    anon = 'anonfile.com+'
    craxpro = 'crax.pro+'
    past = 'pastebin.com+'
    site = 'site:'
    logo()
    print("""
    [1] Anonfile
    [2] Crax Pro
    [3] Pastebin
    [<] Back
    """)
    mode = input('Select: ')
    if mode == '1':
        logo()        
        key = input('Enter your keyword: ')
        webbrowser.open('https://bing.com/search?q='+site+anon+key)
        bing()
    elif mode == '2':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://bing.com/search?q='+site+craxpro+key)
        bing()
    elif mode == '3':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://bing.com/search?q='+site+past+key)
        bing()
    elif mode == '<':
        engine()
    else:
        bing()


engine()
