import threading
import time
import random

import socket

#define function named client with no parameters
def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    port = 50087
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    # (!!!) this must be manually entered to connect to the server 
    server_binding = ('128.6.13.175', port)
    cs.connect(server_binding)

    # open and read in projtestfile.txt as a string
    with open ("proj0testfile.txt", "r") as myfile:
        data = myfile.read()

    #send string that was read in to server
    cs.send(data.encode('utf-8'))
    
    # send message to the client via command line instead
    #msg = raw_input("Enter the message you want to send: ")
    #msg = "Testing"
    #cs.send(msg.encode('utf-8'))

    # Receive data from the server
    data_from_server=cs.recv(100)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    # close the client socket
    cs.close()
    exit()

if __name__ == "__main__":

    #thread to run client function
    t2 = threading.Thread(name='client', target=client)
    t2.start()
    print("Main execution done.")
