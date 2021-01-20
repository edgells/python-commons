from functools import lru_cache

import time
import hashlib
import pickle
from itertools import chain

cache = {}

"""

    缓存装饰器
"""


def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration


def compute_key(function, args, kw):
    """
    将函数名称和参数， 作为缓存标识
    :param function:
    :param args:
    :param kw:
    :return:
    """
    key = pickle.dumps((function.func_name, args, kw))
    return hashlib.sha1(key).hexdigest()


def memoize(duration=10):
    def _memoize(function):
        def __memoize(*args, **kwargs):
            key = compute_key(function, args, kwargs)

            # 是否存在缓存
            if key in cache \
                    and not is_obsolete(cache[key], duration):
                return cache[key]['value']

            result = function(*args, **kwargs)

            cache[key] = {'value': result, 'time': time.time()}

            return result

        return __memoize
    return _memoize

