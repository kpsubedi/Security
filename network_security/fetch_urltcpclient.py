import argparse
import socket

def processInput():
    parser = argparse.ArgumentParser()
    parser.add_argument("Host",help="Host Name",type=str)
    parser.add_argument("Port",help="Port Number",type=int)
    args = parser.parse_args()
    print args.Host + "\t" + str(args.Port)
    print args
    return args.Host, args.Port

def create_socket():
    return socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def fetchPage():
    Host, Port = processInput()
    print Host
    print Port
    sock = create_socket()
    sock.connect((Host,Port))
    sock.send("GET / HTTP/1.1\r\nHost:" + Host + "\r\n\r\n")
    resp = sock.recv(4096)
    #print resp
    return resp
def main():
    response = fetchPage()
    print response

if __name__=='__main__':
    main()

