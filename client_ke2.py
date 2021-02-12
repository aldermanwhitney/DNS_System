import threading
import time
import random

import socket
import sys
import csv

def client():

    #fileObject = open("/ilab/users/kje42/project1/PROJI-DNSRS.txt", "r")
    #data = fileObject.read()
    #print(data)

    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()


    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())


    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    #get info from text file

    #get file object
    f = open("./PROJI-HNS.txt", "r")
    while(True):
	#read next line
        line = f.readline()
        #if line is empty, you are done with all lines in the file
        if not line:
            break
        #you can access the line
        #print(line.strip())
        address = ''
        print("Client sent:")
        for element in range(0, len(line)):
            if (line[element] != " "):
                address += line[element]
        print(address)
        cs.send(address.encode('utf-8'))
    #close file
    f.close


    # Receive data from the server
    data_from_server=cs.recv(100)
    #100 bytes of message it can receive
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    # close the client socket
    cs.close()
    exit()


if __name__ == "__main__":
    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    time.sleep(5)
    print("Client Main Execution Done.")
