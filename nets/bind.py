import socket

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(())  # 当bind 时， 如果socket 还在time wait 或者 close wait的状态， 哪么会提示port 占用
