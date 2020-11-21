# transposition encrypt
# 搞乱消息符号的顺序， 使用消息不可读
import math


def encrypt_message(message, key):
    cipher_text = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            cipher_text[col] += message[pointer]
            pointer += key

    return ''.join(cipher_text)


def decrypt_message(message, key):
    num_of_columns = math.ceil(len(message) / key)
    num_of_rows = key

    #
    num_of_shard_boxes = (num_of_columns * num_of_rows) - len(message)

    plain_text = [''] * num_of_rows
    col = 0
    row = 0

    for symbol in message:
        plain_text[col] += symbol
        col += 1

        if (col == num_of_columns) or \
                (col == num_of_columns - 1) and (row >= num_of_rows - num_of_shard_boxes):
            col = 0
            row += 1

    return ''.join(plain_text)


def test_encrypt():
    message = 'Common sense is not so common.'
    key = 8

    cipher_text = encrypt_message(message, key)

    print(cipher_text)


def test_decrypt():
    message = 'Cenoonommstmme oo snnio. s s c'
    key = 8

    plain_text = decrypt_message(message, key)

    print(plain_text)


if __name__ == '__main__':
    test_decrypt()
