import socket                 
port = 6002              
s = socket.socket()         
host = socket.gethostname()    
s.bind((host, port))          
s.listen(5)                     
print('Server listening....')
conn, addr = s.accept()     	
print('Got connection from', addr)
output = 'Alpha'
conn.sendall(output.encode('utf-8'))
print('Done sending')
conn.close()
s.close()
