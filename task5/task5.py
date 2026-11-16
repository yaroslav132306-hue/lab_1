import time
import numpy as np

try:
    from sumsq import sum_squares_cy, sum_squares_cy_list
except ImportError:
    print("сначала собрать модуль: python setup.py build_ext --inplace")
    raise SystemExit(1)


# 5.1
def sum_squares_py(lst):
    s = 0.0
    for x in lst:
        s += x * x
    return s


def measure(f, data):
    t0 = time.perf_counter()
    r = f(data)
    return r, time.perf_counter() - t0


N = 10 ** 7
arr = np.random.rand(N)
lst = arr.tolist()

r1, t1 = measure(sum_squares_py, lst)
r2, t2 = measure(sum_squares_cy_list, lst)
r3, t3 = measure(sum_squares_cy, arr)
r4, t4 = measure(lambda a: np.dot(a, a), arr)

print(f"N = {N}")
print(f"python (список):       {t1:.3f} с  результат {r1:.4f}")
print(f"cython (список):       {t2:.3f} с  результат {r2:.4f}  x{t1 / t2:.1f}")
print(f"cython (memoryview):   {t3:.3f} с  результат {r3:.4f}  x{t1 / t3:.1f}")
print(f"numpy dot для справки: {t4:.3f} с  результат {r4:.4f}")
