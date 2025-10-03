"""
https://drive.google.com/drive/folders/1jPcRexD2ChIrhd3wsMD7zDrWHYSYKs4X
https://fmhy.net/
"""

import os
import time
from colorama import Fore, Style

page = 1

def cmd(command):
    os.system(command)

def clear():
    os.system('cls')

def loadmenu():
    global page
    global icon

    if page == 1:

        os.system(r'title IllEagle [Page 1 - Piracy]')

        print(f'''{Fore.RED}(                                    
 )\ ) (  (                    (       
(()/( )\ )\(     (    ) (  (  )\  (   
 /(_)|(_|(_)\   ))\( /( )\))(((_)))\  
(_))  _  _((_) /((_)(_)|(_))\ _ /((_) 
|_ _|| || | __(_))((_)_ (()(_) (_))   
 | | | || | _|/ -_) _` / _` || / -_)  
|___||_||_|___\___\__,_\__, ||_\___|  
                       |___/         {Fore.RESET}                   

    PIRACY
[1] > Softwares ECT
[2] > Piracy Goldmine (fmhy)
[3] > DaVinci Resolve Glitch Pack (skape)   
[4] > DaVinci Plugins (Crack)           
''')
    
    elif page == 2:

        os.system(r'title IllEagle [Page 2 - Testicle]')

        print(f'''{Fore.RED}(                                    
 )\ ) (  (                    (       
(()/( )\ )\(     (    ) (  (  )\  (   
 /(_)|(_|(_)\   ))\( /( )\))(((_)))\  
(_))  _  _((_) /((_)(_)|(_))\ _ /((_) 
|_ _|| || | __(_))((_)_ (()(_) (_))   
 | | | || | _|/ -_) _` / _` || / -_)  
|___||_||_|___\___\__,_\__, ||_\___|  
                       |___/         {Fore.RESET}

testicle.
''')
        
    else:
        print('Page Not Found')
        

clear()

print("""
!(page) - change page
""")

while True:
    loadmenu()
    x = input('$ ')
    if x.startswith('!'):
        x = x[1:]
        if x in ["1", "2"]:
            page = int(x)
            print(f'page changed to {page}')
        else:
            print(f'VALUE [{x}] IS NOT A PAGE')

    elif x == '1':
        os.system('start https://appdoze.net')

    elif x == '2':
        os.system('start https://fmhy.net/')

    elif x == '3':
        os.system('start https://drive.google.com/drive/folders/1jPcRexD2ChIrhd3wsMD7zDrWHYSYKs4X')
    
    elif x == '4':
        os.system('start https://drive.google.com/drive/folders/1E1R8VpaGyEy9fn8HJJ4f5Jb3_inx2RUY')
    
    else:
        print(f'{Fore.RED}COMMAND NOT RECOGNISED{Fore.RESET}')
    print('Press any key to Continue...')
    cmd('pause >nul')
    clear()
