# Лабораторная работа. Продвинутый NumPy

| файл | что внутри |
|---|---|
| `task1.py` | float32/float64, машинное эпсилон, катастрофическая отмена |
| `task2.py` | срезы, fancy- и логическая индексация, broadcasting |
| `task3.py` | memmap 1000x1000, чтение строки/столбца, обход по строкам и столбцам |
| `task4.py` | разреженные матрицы CSR / COO / CSC, сравнение скорости с плотной |
| `task5/` | сумма квадратов на Python и на Cython |

## Запуск

```
pip install -r requirements.txt
python task1.py
python task2.py
python task3.py
python task4.py
```

Задание 5 сначала нужно скомпилировать (на Windows нужен Visual Studio Build Tools с C++):

```
cd task5
python setup.py build_ext --inplace
python task5.py
```

В задании 3.3 вместо `%timeit` используется модуль `timeit`, т.к. это обычный скрипт, а не ноутбук.

## Результаты у меня

- 3.3: по строкам ~2.6 мс, по столбцам ~5.4 мс (для F-порядка наоборот)
- 4.4: умножение матриц 1000x1000 (1%): sparse ~1 мс, dense ~17 мс; память 121 КБ против 7.8 МБ
- 5.3: 10^7 элементов: python 0.38 с, cython (список) 0.065 с, cython (memoryview) 0.012 с
