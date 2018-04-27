import socket                   # Import socket module
import ctypes

#print ctypes.windll.shell32.IsUserAnAdmin()


port = 9916                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'







file=open("mytext.txt",'r+')
st=(file.readline())
print "Data before encryption is: ",st
b=list(st)
r=''
for i in b:
   n=str(ord(i))
   m=list(n)
   if len(n)<3:
      m.insert(0,'0')
   for i in m:
      r=r+i
print r
file.close()


n=input("Enter Public Key: ")
e=input("Enter encoding number: ")


abc=pow(int(r), e, n)
print "Data after encryption is: ",abc
file=open("mytext2.txt",'w+')
file.write(str(abc))
file.close()



while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    data = conn.recv(1024)
    

    filename='mytext2.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    print('Server received', repr(data))
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting, Client')
    conn.close()
