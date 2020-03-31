


def test(func):

    def wrap(*args, **kw):

        func(*args, **kw)
        
    return wrap