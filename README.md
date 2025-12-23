# Python-Socket

# Socket Client – Python

A minimal **Python TCP client** that connects to a local server using IPv4 and a stream (TCP) socket.

This repository is intended as a simple starting point for learning or testing socket-based communication in Python.

---

## 📁 Project Structure

```text
.
├── client.py   # Python TCP client
└── README.md   # Project documentation
```

---

## 🧩 Code Overview

```python
#!/bin/python3

# SOCKET
import socket

HOST = '127.0.0.1'
PORT = 7777

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))
```

### Explanation

* `socket.AF_INET` → Uses IPv4 addressing
* `socket.SOCK_STREAM` → Uses TCP (connection-oriented)
* `HOST = 127.0.0.1` → Localhost (same machine)
* `PORT = 7777` → Port where the server must be listening
* `connect((HOST, PORT))` → Establishes the TCP connection to the server

---

## ⚙️ Requirements

* Python **3.x**
* A TCP server listening on `127.0.0.1:7777`

No external libraries are required.

---

## ▶️ How to Run

1. Start a TCP server on port `7777`
2. Run the client:

```bash
python3 client.py
```

If the connection succeeds, the client will connect silently.
If no server is running, a `ConnectionRefusedError` will be raised.

---

## 🧪 Example Test Server (Optional)

You can test the client with a simple Python server:

```python
import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print(f"Connected by {addr}")
```

---

## 🚀 Possible Improvements

* Add error handling (`try/except`)
* Send and receive data (`send()`, `recv()`)
* Close the connection properly (`conn.close()`)
* Make host and port configurable via CLI arguments

---

## 📜 License

This project is released under the **MIT License**.

---

## 👤 Author

Created by **Matteo Sabaudo**

Feel free to fork, modify, and improve this project.
