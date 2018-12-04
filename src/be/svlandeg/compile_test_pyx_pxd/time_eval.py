import combo_test
import time


def time_eval(x):
    start = time.time()
    combo_test.eval_cy(x)
    end = time.time()

    print("combo time", end-start)


if __name__ == '__main__':
    # pure python in py: around 0.4s
    # pure python in pyx compiled to pyd: around 0.3s
    # python + cdef definition in pyx compiled to pyd: virtually 0s
    time_eval(x=5000000)

