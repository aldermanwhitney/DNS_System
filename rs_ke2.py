import threading
import time
import random

import socket
import sys
import csv
import json

from client import *
# You need to choose the appropriate data structure to store the values for each entry
# The client always connects first to RS, sending the queried hostname as a string
# The RS program does a look up in its DNS_table, and if there is a match,sends the entry as a string

# (1) client connects first to RS
# (2) RS looks up in its DNS_table
#     if there is a match = Hostname IPaddress A
#     if there is no match = TSHostname - NS

# (3) sends answer to client server

def server():
#server opens a socket: a method for two way communication in a program within a network
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #1st parameter: ipv4
        #2nd parameter: tcp (transport protocol)
        print("[RS]: Server socket created") 
        #if successful => server socket created
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    
    #server_binding = ('', 50087)
    
    rsListenPort = sys.argv[1]
    server_binding = ('', int(rsListenPort))
    ss.bind(server_binding)
    #binding socket to port
    
    #get info from text file

    #get file object
    f = open("./PROJI-DNSRS.txt", "r")
    dict_ip = {}
    dict_flag = {}
    while(True):
	#read next line
        line = f.readline()
        #if line is empty, you are done with all lines in the file
        if not line:
            break
        #you can access the line
        #print(line.strip())
        address = ''
        ip = ''
        flag = ''
        count = 0
        for element in range(0, len(line)):
            if (line[element] != " "):
                if (count == 0):
                    address += line[element] 
                if (count == 1):
                    ip += line[element] 
                if (count == 2):
                    flag += line[element]
            else:
                count += 1

        #populate RS TABLE
        if (count == 2):
           dict_ip[address] = ip
           dict_flag[address] = flag
                
    
    #close file
    f.close
    print(dict_ip)
    print(dict_flag)

    #client would need port to access anything
    ss.listen(1)
    #how many connections are allowed to have which is 1
    host = socket.gethostname()
    print("[RS]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[RS]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[RS]: Got a connection request from a client at {}".format(addr))
    #accepts the connection
    #ss.accept() #=> returns accepted socket and the address you're connecting to 

    # receive and send message to the client.  
    data_from_client=csockid.recv(100)
    print("[RS]: Root server recieved: " + str(data_from_client));
    data = ''
    data = data_from_client.decode()
    data = data.rstrip()

    if data in dict_ip:
       msg = data + ' ' + dict_ip[str(data)] + ' ' + dict_flag[str(data)]
       csockid.send(msg.encode('utf-8'))

    if data not in dict_ip:
        msg = data + ' ' + "-" + ' ' + "Error:HOST NOT FOUND"
        csockid.send(msg.encode('utf-8'))

    # Close the server socket
    ss.close()
    exit()   

if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()

    time.sleep(5)
    print("RS Main Execution Done.")
