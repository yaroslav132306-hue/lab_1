import numpy as np

np.random.seed(42)

# 2.1
A = np.random.randint(-10, 10, size=(4, 5))
print("A =\n", A)
print("\n2.1")
print("вторая строка:", A[1])
print("столбец 3:", A[:, 3])
print("строки 1-3, столбцы 2-4:\n", A[1:4, 2:5])

# 2.2 fancy-индексация
rows = [0, 2, 3]
cols = [1, 4]
print("\n2.2")
print("np.ix_ (все пересечения строк и столбцов):\n", A[np.ix_(rows, cols)])
# то же самое через broadcasting индексов
print("через A[[[0],[2],[3]], [1, 4]]:\n", A[np.array(rows)[:, None], cols])

# 2.3 логическая индексация
print("\n2.3")
A2 = A.copy()
print("отрицательных было:", (A2 < 0).sum())
A2[A2 < 0] = 0
print(A2)

# 2.4 broadcasting
print("\n2.4")
B = np.arange(4).reshape(4, 1) * 10
C = np.arange(5).reshape(1, 5)
print("B", B.shape, "\n", B)
print("C", C.shape, "\n", C)
res = B + C
print("B + C ->", res.shape, "\n", res)
# (4,1) и (1,5): справа налево 1 vs 5 -> 5, 4 vs 1 -> 4, итог (4,5)
