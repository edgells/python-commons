import socket


"""
    so
"""

HOST = '0.0.0.0'
PORT = 8080

# create tcp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))

sock.listen(128)  # 最多能等待的连接数

