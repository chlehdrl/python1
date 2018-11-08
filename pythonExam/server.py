import socket,sys,math
# 서버
def string_xor(data,key):
            j=0
            result=''

            for i in range(len(data)):
                result+= chr(ord(data[i])^ord(key[j]))
                j+=1
                if (j== len(key)):
                            j=0
            return result

s=socket.socket()
s.bind(('',5666))
s.listen(1)
print('Socket Listen Start')

connector, addr = s.accept()
key="password"
while 1:
            data = connector.recv(1024)
            if not data: break

            decryptMessage = string_xor(data.decode('utf-8'),key)
            print ("Received Message :", decryptMessage)


            data = input("Message:");
            encryptMessage = string_xor(data,key)
            connector.send(data.encode('utf-8'));
s.close()

