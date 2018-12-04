import cy_script
import py_script
import time


def time_eval(x):
    cy_start = time.time()
    cy_script.eval_cy(x)
    cy_end = time.time()

    py_start = time.time()
    py_script.eval_py(x)
    py_end = time.time()

    print("cy vs py", cy_end-cy_start, py_end-py_start)


if __name__ == '__main__':
    time_eval(x=5000000)

