import os
import colorama
colorama.init(autoreset=True)

from colorama import Fore

class PrintClass:
  def __init__(self) -> None:
    pass
  
  def clean_screen(self):
    os.system("clear")

  def print_big_name(self):
    print('                                                                                                ')
    print(Fore.GREEN + " ############   ####     ###   ############   ############   ####      ###   ###   ############ ")
    print(Fore.GREEN + " ############   #####    ###   ############   ############   #####     ###   ###   ############ ")
    print(Fore.GREEN + " ###      ###   ######   ###       ####       ###      ###   ######    ###   ###   ###      ### ")
    print(Fore.GREEN + " ###      ###   ### ###  ###       ####       ###      ###   ### ###   ###   ###   ###      ### ")
    print(Fore.GREEN + " ############   ###  ### ###       ####       ###      ###   ###  ###  ###   ###   ###      ### ")
    print(Fore.GREEN + " ############   ###   ######       ####       ###      ###   ###   ### ###   ###   ###      ### ")
    print(Fore.GREEN + " ###      ###   ###    #####       ####       ###      ###   ###    ######   ###   ###      ### ")
    print(Fore.GREEN + " ###      ###   ###     ####       ####       ############   ###     #####   ###   ############ ")
    print(Fore.GREEN + " ###      ###   ###      ###       ####       ############   ###       ###   ###   ############ ")
    print('                                                                                                ')


  