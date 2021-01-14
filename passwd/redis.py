import random
import string


def random_string(char=string.ascii_letters, size=64):
    return "".join([random.choice(char) for _ in range(size)])


redis_passwd = "OmSOyZpKXczQqdlTUTlKbrBuSRVjUWWQmaFZEpfneBgslEBimIGaRUDMOhTLaFFw"
print(random_string())
