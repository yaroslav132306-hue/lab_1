import os
import timeit
import numpy as np

FNAME = "data.dat"
N = 1000

# 3.1 создаём memmap файл и заполняем случайными числами
mm = np.memmap(FNAME, dtype=np.float64, mode="w+", shape=(N, N))
rng = np.random.default_rng(0)
# пишем кусками по 100 строк, чтобы не держать весь массив в памяти
for i in range(0, N, 100):
    mm[i:i + 100] = rng.random((100, N))
mm.flush()
del mm
print("3.1")
print("файл:", FNAME, "размер:", os.path.getsize(FNAME) / 1024 ** 2, "МБ")

# 3.2 открываем только на чтение и берём одну строку и один столбец
m = np.memmap(FNAME, dtype=np.float64, mode="r", shape=(N, N))
row = np.array(m[10])       # с диска читается только эта строка
col = np.array(m[:, 10])    # тут 1000 чисел вразброс (шаг 8000 байт)
print("\n3.2")
print("строка 10, первые 5:", row[:5])
print("столбец 10, первые 5:", col[:5])
print("m[10, 10] =", m[10, 10], row[10] == col[10])

# 3.3 обход по строкам и по столбцам
# в скрипте %timeit нет, поэтому через модуль timeit (в jupyter то же самое
# делается командой %timeit by_rows(arr))
arr = np.array(m)   # уже в памяти, C-порядок


def by_rows(a):
    s = 0.0
    for i in range(a.shape[0]):
        s += a[i, :].sum()
    return s


def by_cols(a):
    s = 0.0
    for j in range(a.shape[1]):
        s += a[:, j].sum()
    return s


print("\n3.3")
for name, f in [("по строкам", by_rows), ("по столбцам", by_cols)]:
    t = min(timeit.repeat(lambda: f(arr), number=10, repeat=5)) / 10
    print(f"{name}: {t * 1000:.2f} мс")

# для Fortran-порядка картина наоборот
arr_f = np.asfortranarray(arr)
print("тот же массив в F-порядке:")
for name, f in [("по строкам", by_rows), ("по столбцам", by_cols)]:
    t = min(timeit.repeat(lambda: f(arr_f), number=10, repeat=5)) / 10
    print(f"{name}: {t * 1000:.2f} мс")

print("""
Вывод: numpy по умолчанию хранит массив построчно (C-order). Строка лежит
в памяти подряд, процессор подгружает её в кэш целыми линиями по 64 байта
и сразу использует все 8 чисел из линии. Столбец же разбросан с шагом
N*8 = 8000 байт, на каждое число приходится новая кэш-линия, поэтому
обход по столбцам медленнее. Для Fortran-массива всё зеркально.""")

del m
os.remove(FNAME)
