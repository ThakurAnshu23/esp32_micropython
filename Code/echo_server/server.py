#echo server using TCP in Python

import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 54321

# Creat socket

try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((IP,PORT))
    sock.listen()
    print(f"Server is up and running at {IP}:{PORT}")
except Exception as e:
    print("Error in socket creation:",e)
    sys.exit()




#handle the client
while True:
    try:
        client,addr = sock.accept()
        print("Client connected from : ",addr[0],":",addr[1])
        while True:
            try:
                msg = client.recv(1024)
                if not msg:
                    print("No data recieved")
                    break
                print(addr[0],":",addr[1],">> ",msg)
                client.send(msg)
            except Exception as e:
                print("Error in send/recv: ",e)
                break
    except KeyboardInterrupt:
        print("closing client connection")
        client.close()
        break       
    except Exception as e:
        print("Error in handling clint :",e)
        break    

sock.close()
sys.exit()
