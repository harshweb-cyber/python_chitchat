# python_chitchat 💬🐍

**python_chitchat** is a simple multithreaded Python chat application that allows two users to communicate over a local network using TCP sockets. It's built using Python's `socket` and `threading` libraries.

---

## 📦 Features

- Bidirectional chat between server and client.
- Threaded message sending and receiving.
- Minimal, clean code with no third-party dependencies.
- Simple to run and test on localhost.

---

## 📁 Project Structure
├── server.py # Starts a chat server and waits for a connection. 
|── client.py # Connects to the server and starts chatting.

## 🚀 How to Run

### On Linux/macOS

#### Start the Server
```bash
python3 server.py

You should see:
Listening...

Start the Client (in a new terminal or on another device)
python3 client.py


####💻 How to Run on Windows

#####Start the Server
python server.py

#####Start the client
python client.pys
