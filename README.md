0. Please write down the full names and netids of both your team members.
    Karen Elenjickal - kje42
    Whitney Alderman - wa125
1. Briefly discuss how you implemented your recursive client functionality.
    Our recursive client continuously requests for a connection and accepts messages from RS and TS within
    a while loop until it finishes reading the PROJI-HNS.txt file.
2. Are there known issues or functions that aren't working currently in your
   attached code? If so, explain.
   There aren't any issues/functions that aren't working.

3. What problems did you face developing code for this project?
    One problem we faced was when a continuous request was asked to RS from the client but the connection ended to soon on RS so we had RS accept messages of 100 bytes until the       client sent a message 'stop' to RS
    to end loop.
4. Reflect on what you learned by working on this project. 
    We've learned how to implement a socket connection between the client and TS server and the client and the RS server. We've also learned how to keep that connection opened.
