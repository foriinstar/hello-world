import socket,time

s = socket.socket()
s.connect(('192.168.2.157',8888))
Flag = True
while Flag:
    print(s.recv(1024))
    inp = input('input datas:')
    if inp == 'exit':
        Flag = False
    else:
        s.send(bytes(inp,encoding='utf-8'))
s.close()
