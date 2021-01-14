import socket
import pprint


infolist = socket.getaddrinfo("baidu.com", 'www')
pprint.pprint(infolist)