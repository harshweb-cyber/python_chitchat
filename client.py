#!/usr/bin/env python3

import socket
import threading

def send_msg():
    while True:
        try:
            msg = input().encode()
            s.send(msg)
        except (ConnectionResetError, BrokenPipeError):
            print("[!] Connection lost while sending.")
            break
        except Exception as e:
            print(f"[!] Error in send_msg: {e}")
            break

def recv_msg():
    while True:
        try:
            received = s.recv(1024)
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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting...")

while True:
    try:
        s.connect(("127.0.0.1", 8888))
        break
    except ConnectionRefusedError:
        continue
    except Exception as e:
        print(f"[!] Unexpected error while connecting: {e}")
        break

print("Connected to server.")

t1 = threading.Thread(target=send_msg)
t1.start()

recv_msg()

s.close()
