import socket

#host = "www.google.com"
host = "www.memphis.edu"
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host,port))
sock.send("GET / HTTP/1.1\r\nHost: www.memphis.edu\r\n\r\n")

resp = sock.recv(4096)

print resp
  
