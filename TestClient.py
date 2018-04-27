import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 9916                    # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

with open('received_file.txt', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print data
        d = input("Enter your Private Key: ")
        n = input("Enter your Public Key: ")
        c = int(data)
        data=pow(c, d, n)
        print "Decoding....."
        c=int(data)
        x=str(c)
        v=len(x)
        l=''
        if v%3!=0:
            j=list(x)
            j.insert(0,'0')
            for i in j:
                l=l+i
            x=l
        b=''     
        v=len(x)
        for i in range(0,v,3):
            if x[i]=='0':
                b=b+chr(int(x[i+1:i+3]))
            else:
                b=b+chr(int(x[i:i+3]))
        print "Data received from server is: ",b
        if not data:
            break
        
        # write data to a file
        f.write(str(data))

f.close()
print('Successfully got the file')
s.close()
print('connection closed')
