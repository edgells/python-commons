import string
import time

"""
    凯撒加密实质上是一种字符位移的明文混淆
    核心点：
        1. key 的大小， 本身由加密范围决定。 
        2. 对于消息的处理， 需要根据在范围和不在范围的情况处理
"""

key = 13
# 密钥在 0-25
mode = 'encrypt'

LETTERS = string.ascii_uppercase


def caeser_encrypt(message: str):
    translated = ''

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == 'encrypt':
                num = num + key

            elif mode == 'decrypt':
                num = num - key

            if num >= len(LETTERS):
                num = num - len(LETTERS)

            elif num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]

        else:
            translated = translated + symbol

    return translated


def test_caeser_encrypt():
    message = "this is my secret message."
    message = message.upper()  # 如果是大小写敏感的话不需要处理

    encrypt_str = caeser_encrypt(message)
    print(encrypt_str)


if __name__ == '__main__':
    test_caeser_encrypt()
