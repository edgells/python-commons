import base64

"""
    base64 将二进制字符转换成可打印的字符串
"""
print(bytes(b'helloworld').decode())
print(base64.b64encode(b"hello world").decode())
