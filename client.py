import socket                   
s = socket.socket()            
host = socket.gethostname()    
port = 6002                   
s.connect((host, port))
print('receiving data...')
data = s.recv(1024)
d = data.decode("utf-8")
print('data=%s'%str(data))
print(d)
print('Successfully got Data')
s.close()
print('connection closed')
