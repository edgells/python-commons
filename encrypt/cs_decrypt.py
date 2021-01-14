import string

LETTERS = string.ascii_uppercase
print(string.ascii_uppercase)
print(string.ascii_lowercase)


def caeser_decrypt(message: str):
    for key, _ in enumerate(LETTERS):
        translated = ''

        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key

                if num < 0:
                    num = num + len(LETTERS)

                translated += LETTERS[num]

            else:
                # 如果字符不存在加密的区间， 直接转换
                translated += symbol

        print('Key #%0d: %s' % (key, translated))


def test_caeser_decrypt():
    msg = 'GUVF VF ZL FRPERG ZRFFNTR.'

    caeser_decrypt(msg)


if __name__ == '__main__':
    test_caeser_decrypt()
