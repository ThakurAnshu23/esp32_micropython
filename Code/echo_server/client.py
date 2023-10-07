#Client for echo server using TCP in Python
import socket
import sys

#server condition

IP = socket.gethostbyname("192.168.167.187")
PORT = 55203

# Creat socket

try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((IP,PORT))
    
    print(f"client is connected")
except Exception as e:
    print("Error in socket creation:",e)
    sys.exit()




#client operation
while True:
    try:
        input_message = input("Enter here: ")
        sock.send(input_message.encode("utf-8"))
        recv_msg = sock.recv(1024)
        if not recv_msg:
            print("No msg recieved")
            break
        print("echo >> ",recv_msg.decode("utf-8"))
    except Exception as e:
        print("Error in client operation :",e)
        break

       
       
    except KeyboardInterrupt:
        print("closing client connection")
        break  

sock.close()
sys.exit()
