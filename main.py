from pyautogui import press, write
from time import sleep, time
from os import system

def banner():
    system('cls')
    print("""
     _____                           _____                                          
    / ___/ __  ______  ___  _____   / ___/____  ____ _____ ___  ____ ___  ___  _____
    \__ \ / / / / __ \/ _ \/ ___/   \__ \/ __ \/ __ `/ __ `__ \/ __ `__ \/ _ \/ ___/
    ___/ / /_/ / /_/ /  __/ /      ___/ / /_/ / /_/ / / / / / / / / / / /  __/ /    
  /____/\__,_/ .___/\___/_/      /____/ .___/\__, _/_/ /_/ /_/_/ /_/ /_/\___/_/     
            /_/                      /_/  v2022.0                                         
            
                    [ * ] Coded by WanZ [ * ]
            [ ! ] Use only for your friends [ ! ]
            
        """)
banner()

msg = input("Enter msg: ")
count = input("Count: ")
for i in range(1, 4):
    print("Firing in " + str(i))
    sleep(1)
start_time = time()
for i in range(int(count)):
    write(str(msg), interval=0)
    press('enter')
    print("[ + ] {}/{} DONE".format(i,count) )


banner()
print("All {} {} done in {}s ! \n Thanks for using Super Spammer v2022.0.\nPlease alert that developer won't responsible for any problem that you cause by this tool".format(count, msg, str(round((time()-start_time), 2))))