#!/usr/bin/env python
# --------------------------------------------------
# Nathália Magre Guerra Pinto
# Programação de Sistemas Robóticos
# Universidade de Aveiro, 2022-2023
# -------------------------------------------------
import socket
import time

# initialization of the socket library
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP/IP socket
local_hostname = socket.gethostname()  # retrieve local hostname
local_fqdn = socket.getfqdn()  # get fully qualified hostname
ip_address = socket.gethostbyname(local_hostname)  # get the according IP address

# connecting with the server
server_address = (ip_address, 23456)  # bind the socket to the port 23456, and connect
sock.connect(server_address)
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# Define a dog to be sent
import ex2_dogLib
dog = ex2_dogLib.Dog("Dalila", "brown", "5")
dog.addBrother("Rex")
dog.addBrother("Zeus")
print(ex2_dogLib.Dog)

# Define example data to be sent to the server

# serialization or marshalling
message = dog.name
message += ","
message += str(dog.age)
message += ","
message += dog.color
for brother in dog.brothers:
    message += "," + brother

# send the message
while True:
    print("Sending message: " + str(message))
    sock.sendall(message)
    time.sleep(2)

sock.close()  # close connection