import requests
import threading
import time
import colorama
from colorama import Fore, Back, Style
import sys


def dir_enumeration(dir):
        port = 8000
        # {sys.argv[1]} allows u to get input from cli [1] point to actual spot in entered command
        url_path = f"http://{sys.argv[1]}:{port}/{dir}"
        try:
            request = requests.get(url_path)
            if request.status_code == 404:
                pass
            else:
                print(f"{Fore.YELLOW}{Style.BRIGHT} /{dir} [{request.status_code}] founded directories ")
        except requests.ConnectionError as _ex:
            print(f"{Fore.RED}\n{_ex}")

def main():
    with open("path to your dictionary", "r") as file:
        # .splitlines() method, transforms into list
        directories = file.read().splitlines()
        for directory in directories:
            thread = threading.Thread(target=dir_enumeration, args=(directory,))
            thread.start()
            # rate limiting
            #time.sleep(0.1)

if __name__ == "__main__":
    main()