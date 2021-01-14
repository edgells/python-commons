import socket


HOST = '0.0.0.0'
PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(128)
# set timeout 会被继承


while 1:
    cli_sock, addr = sock.accept()
    cli_sock.settimeout(5)
    # new cli
    print("link from", addr)

    data = b""
    while 1:
        recv_data = cli_sock.recv(1499)

        # 数据接收完毕
        if not recv_data:
            break

        data += recv_data

    print(data)

    # 关闭客户端sock
    cli_sock.close()
