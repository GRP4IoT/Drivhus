from threading import Thread
from time import sleep
from colorama import Fore
def f1():
    while True:
       print(Fore.GREEN + "f1 running")
       sleep(1)


t1 = Thread(target=f1, daemon=True)
t1.start()


while True:
    print(Fore.YELLOW + "running main thread")
    sleep(1)
