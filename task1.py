import numpy as np

# 1.1 сумма 0.1 + 0.2 + 0.3 во float32
a = np.array([0.1, 0.2, 0.3], dtype=np.float32)
s = a.sum()
print("1.1")
print("массив:", a)
print("сумма float32:", repr(s), "| точнее:", f"{float(s):.20f}")
print("ожидаем 0.6, разница:", abs(float(s) - 0.6))
# s == 0.6 тут дало бы True, т.к. numpy приведёт 0.6 к float32, поэтому сравниваем в float64
print("float(s) == 0.6 ?", float(s) == 0.6)
print("np.isclose(s, 0.6) ?", np.isclose(s, 0.6))

b = np.array([0.1, 0.2, 0.3], dtype=np.float64)
print("для сравнения float64:", f"{b.sum():.20f}", "разница:", abs(b.sum() - 0.6))
print()

# 1.2 машинное эпсилон
print("1.2")
for t in (np.float32, np.float64):
    info = np.finfo(t)
    print(f"{t.__name__}: eps = {info.eps}, знаков после запятой ~{info.precision}")

# проверка что 1 + eps != 1, а 1 + eps/2 уже == 1
eps32 = np.finfo(np.float32).eps
one = np.float32(1.0)
print("1 + eps   != 1:", one + eps32 != one)
print("1 + eps/2 == 1:", one + eps32 / np.float32(2) == one)
print()

# 1.3 катастрофическая отмена
print("1.3")
x = 1.0 + 1e-7
y = 1.0
exact = 1e-7

d32 = np.float32(x) - np.float32(y)
d64 = np.float64(x) - np.float64(y)
print("точно:        ", exact)
print("float32 x - y:", d32, "отн. ошибка:", abs(d32 - exact) / exact)
print("float64 x - y:", d64, "отн. ошибка:", abs(d64 - exact) / exact)

# классический пример: 1 - cos(t) при маленьком t
t = np.float32(1e-4)
bad = np.float32(1) - np.cos(t)
good = np.float32(2) * np.sin(t / np.float32(2)) ** 2   # та же формула, но без вычитания
print("\n1 - cos(1e-4), float32:")
print("в лоб:         ", bad)
print("через 2sin^2:  ", good)
print("правильно ~    ", 1e-4 ** 2 / 2)
# в лоб получается 0 (или мусор) - cos(t) почти 1, и все значащие цифры
# при вычитании сокращаются
