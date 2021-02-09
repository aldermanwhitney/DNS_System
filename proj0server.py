import threading
import time
import random
from client import *

import socket

#define function named server with no parameters
def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    #Server creates socket, binds, listens and then accepts a connection
    server_binding = ('', 50087)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))

    #code execution will halt at accept() until the client connects
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    # Recieve string from client
    data_from_client = csockid.recv(100)
    print("[S]: Data received from client: {}".format(data_from_client.decode('utf-8')))
    
    # send reversed string to the client.  
    msg = data_from_client.decode('utf-8')[::-1]
    csockid.send(msg.encode('utf-8'))

    # Close the server socket
    ss.close()
    exit()

if __name__ == "__main__":
    
    #thread to run server() function
    t1 = threading.Thread(name='server', target=server)
    t1.start()
    time.sleep(random.random() * 5)
    print("Main Execution Done.")
