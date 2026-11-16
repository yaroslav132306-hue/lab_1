# cython: language_level=3, boundscheck=False, wraparound=False

def sum_squares_cy(double[:] arr):
    cdef Py_ssize_t i, n = arr.shape[0]
    cdef double s = 0.0
    for i in range(n):
        s += arr[i] * arr[i]
    return s


def sum_squares_cy_list(list lst):
    # вариант для обычного списка, как в python-версии
    cdef double s = 0.0
    cdef double x
    for x in lst:
        s += x * x
    return s
