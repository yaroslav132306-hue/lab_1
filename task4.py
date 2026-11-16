import timeit
import numpy as np
from scipy import sparse

# 4.1 CSR 5x5, плотность 20% -> 5 ненулевых
S = sparse.random(5, 5, density=0.2, format="csr", random_state=1)
print("4.1")
print("CSR, ненулевых:", S.nnz)
print("data:   ", S.data)
print("indices:", S.indices)
print("indptr: ", S.indptr)
print(S.toarray().round(3))

# 4.2
coo = S.tocoo()
csc = S.tocsc()
print("\n4.2")
print("COO row: ", coo.row)
print("COO col: ", coo.col)
print("COO data:", coo.data)
print("CSC data:   ", csc.data)
print("CSC indices:", csc.indices)
print("CSC indptr: ", csc.indptr)
print("матрицы совпадают:", np.allclose(coo.toarray(), csc.toarray()))

# 4.3 умножение на плотный вектор
v = np.arange(1, 6, dtype=float)
print("\n4.3")
print("v =", v)
print("S @ v =", S @ v)
print("проверка через плотную:", S.toarray() @ v)

# 4.4 1000x1000, плотность 0.01
n = 1000
Sb = sparse.random(n, n, density=0.01, format="csr", random_state=2)
Db = Sb.toarray()
x = np.random.rand(n)
M = sparse.random(n, n, density=0.01, format="csr", random_state=3)
Md = M.toarray()

print("\n4.4")
print("ненулевых:", Sb.nnz)
mem_sparse = Sb.data.nbytes + Sb.indices.nbytes + Sb.indptr.nbytes
print(f"память: sparse {mem_sparse / 1024:.0f} КБ, dense {Db.nbytes / 1024:.0f} КБ")


def t(f, k):
    return min(timeit.repeat(f, number=k, repeat=3)) / k * 1000


print(f"матрица * вектор:  sparse {t(lambda: Sb @ x, 200):.3f} мс, "
      f"dense {t(lambda: Db @ x, 200):.3f} мс")
print(f"матрица * матрица: sparse {t(lambda: Sb @ M, 5):.2f} мс, "
      f"dense {t(lambda: Db @ Md, 5):.2f} мс")
print(np.allclose((Sb @ M).toarray(), Db @ Md))
# при 1% заполнения sparse хранит и перемножает только ненулевые,
# поэтому выигрывает и по памяти, и по скорости
