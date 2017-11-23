import time

__all__ = ('timeit', 'is_int', 'is_w2')


def timeit(func):
    def timed(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("method: {a}, time : {b: 0.6f} sec".format(a=func.__name__,
                                                         b=t2-t1))
        return result
    return timed


def is_w2(func):
    def temp(*args, **kwargs):
        print("w2_에서 필요한 함수입니다.")
        return func(*args, **kwargs)

    return temp


def is_int(func):
    def temp(*args, **kwargs):
        print("int_에서 필요한 함수입니다.")
        return func(*args, **kwargs)

    return temp
