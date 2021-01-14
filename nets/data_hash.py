import random
import string


def random_string(char=string.ascii_lowercase):
    return "".join([random.choice(char) for _ in range(4)])


load_balance = {}


def hash_shard(word):
    server_hash = (hash(word) % 4)
    load_balance["server%d" % server_hash] = load_balance.get("server%d" % server_hash, 0) + 1


def md5_shard(word):
    return "server md5 %d" % (hash(word) % 4)


if __name__ == '__main__':
    for _ in range(4):
        hash_list = [random_string() for _ in range(100)]

        for word in hash_list:
            hash_shard(word)

    print(load_balance)
