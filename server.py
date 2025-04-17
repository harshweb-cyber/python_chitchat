#!/usr/share/python3

import socket
import threading

def send_msg():
    while True:
        try:
            msg = input().encode()
            client.send(msg)
        except (ConnectionResetError, BrokenPipeError):
            print("[!] Connection lost while sending.")
            break
        except Exception as e:
            print(f"[!] Error in send_msg: {e}")
            break

def recv_msg():
    while True:
        try:
            received = client.recv(1024)
            if not received:
                print("[!] Server disconnected.")
                break
            print(received.decode())
        except (ConnectionResetError, OSError):
            print("[!] Connection lost while receiving.")
            break
        except Exception as e:
            print(f"[!] Error in recv_msg: {e}")
            break

        

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("127.0.0.1",8888))
print("Listening...")
s.listen(1)
client,addr = s.accept()
print(f"Connected to {addr}")

t1 = threading.Thread(target=send_msg)
t1.start()
recv_msg()
