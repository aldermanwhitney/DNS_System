import threading
import time
import random

import socket
import sys
import csv

def client():

    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
    rsHostname = sys.argv[1]
    rsListenPort = sys.argv[2]
    tsListenPort = sys.argv[3]
    print("rsHostname: " + rsHostname)
    print("rsListenPort " + rsListenPort)
    print("tsListenPort " + tsListenPort)
    localhost_addr = socket.gethostbyname(socket.gethostname())
    server_binding = (rsHostname, int(rsListenPort))
    cs.connect(server_binding)
    f = open("./PROJI-HNS.txt", "r")
    file = open("./RESOLVED.txt", "w")
    count1 = len(open("/ilab/users/kje42/project1/PROJI-HNS.txt").readlines(  ))
    print("COUNT1") 
    print(count1)
    while(True):
    #read next line
        line = f.readline()
        if not line:
            break
        address1 = ''
        for element in range(0, len(line)):
               address1 += line[element]
        cs.send(address1.encode('utf-8'))
        print("Client sent:" + address1)
        data_from_server=cs.recv(100)
        print("[C]: Data received from root server: {}".format(data_from_server.decode('utf-8')))
        received_data = data_from_server.decode('utf-8')
        file.write(received_data) 
     

        # This is the case where the client recieved a message from
        # the root server indicating that the IP address is not known by the root
        # ie localhost - NS
        #must forward request to TS
        suffix = "NS";                   
        if suffix in received_data:
            try:
                cts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print("[C]: Client-TS socket created")
            except socket.error as err:
                print('socket open error: {} \n'.format(err))
                exit()       
            #parse out ts hostname from response
            # and create client/TS socket from it
            tsHostname = received_data.split(' ',1)[0]
            # connect client to the TS
            ts_server_binding = (tsHostname, int(tsListenPort))
            cts.connect(ts_server_binding)
            #send query to TS server
            cts.send(address1.encode('utf-8'))
            #recieve reply from TS server
            data_from_TSserver=cts.recv(100)
            print("[C]: Data received from TS server: {}".format(data_from_TSserver.decode('utf-8')))   
            #write response into RESOLVED.txt file
            file = open("./RESOLVED.txt", "w") 
            file.write(data_from_TSserver) 
    file.close()      
    f.close
    cs.close()
    exit()


if __name__ == "__main__":
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    time.sleep(5)
    print("Client Main Execution Done.")