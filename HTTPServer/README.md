(A) To be able to view these files on a local server: 
1) Open WAMPServer
2) Run LocalServer.py
3) Open "127.0.0.1:HPort" or "localhost:HPort" (#HPort value is mentioned in LocalServer.py)
   Eg: 127.0.0.1:8008



(B) To be able to open localserver on mobile or any device:
1) Make those devices connected to the same network(Create a hotspot from 
	computer and make the mobile connect to that)
2) Open cmd and type 'ipconfig'
3) Note down the IPv4 address
4) Run WAMPServer
5) Run LocalServer.py
6) Open web browser and type "IPv4 address:HPort" (#HPort value is mentioned in LocalServer.py)
   Eg: 192.168.137.1:8008
