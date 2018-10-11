import socket, sys, math
#클라이언트
def string_xor(data,key):
        j=0
        result=''

        for i in range(len(data)):
                result+=chr(ord(data[i])^ord(key[j]))
                j+=1
                if(j==len(key)):
                        j=0
        return result

key="password"

HOST ='127.0.0.1'
PORT = 5666

s= socket.socket()
s.connect((HOST,PORT))


while 1:
        data = input("Message:")
        encryptMessage = string_xor(data,key)
        s.send(data.encode('utf-8'))

        data = s.recv(1024)
        if not data: break

        decryptMessage = string_xor(data.decode('utf-8'),key)
        print("Received Message:",data.decode('utf-8'))
s.close();
