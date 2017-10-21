import time

__all__ = ('timeit', )


def timeit(func):
    def timed(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("method: {a}, time : {b: 0.6f} sec".format(a=func.__name__,
                                                         b=t2-t1))
        return result
    return timed