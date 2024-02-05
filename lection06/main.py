# import socket
# import threading
# from time import sleep

# ya_sock = socket.socket()
# ya_sock.connect(("87.250.250.242", 443))
# ya_sock.send(b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n")

# data_in = b""


# def receiving():
#     global data_in
#     while True:
#         data_chunk = ya_sock.recv(1024)
#         data_in = data_in + data_chunk


# rec_thread = threading.Thread(target=receiving)
# rec_thread.start()

# sleep(6)
# # rec_thread.join()
# print(data_in)
# ya_sock.close()

import socket
import threading
from time import sleep

ya_sock = socket.socket()
ya_sock.connect(("87.250.250.242", 443))
data_in = b""


def receiving():
    global data_in
    while True:
        data_chunk = ya_sock.recv(1024)
        data_in = data_in + data_chunk


with ya_sock:
    ya_sock.send(b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n")
    rec_thread = threading.Thread(target=receiving)
    rec_thread.start()
    sleep(4)
    print(data_in)
