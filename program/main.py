import random as rnd

import matplotlib.pyplot as plt
import numpy as np
import timeit


def findmin():
    min = randmax
    for i in a:
        if min > i:
            min = i
    return min


def findmax():
    max = 0
    for i in a:
        if max < i:
            max = i
    return max


def create_graph(b, c, aur, bur):
    plt.scatter(b, c, s=5)
    y_line = aur * np.array(b) + bur
    plt.plot(b, y_line, color='red')
    plt.title("График")
    plt.xlabel("X-ось")
    plt.ylabel("Y-ось")
    correlation_coefficient = np.corrcoef(c, b)[0, 1]
    return correlation_coefficient


correlation_v = []
# Цикл нужен для создания двух графиков, один при среднем случае, второй при худшем
for namegraph in ["Минимум", "Максимум"]:
    x = [i for i in range(10, 10001, 10)]
    time = []
    x2 = []
    xtime = []
    randmax = 1000000
    if namegraph == "Минимум":
        for i in x:
            a = [rnd.randint(0, randmax) for j in range(i)]
            time.append(timeit.timeit(lambda: findmin(), number=10)/10)
    else:
        for i in x:
            a = [rnd.randint(0, randmax) for j in range(i)]
            time.append(timeit.timeit(lambda: findmax(), number=10)/10)

    # Вычисление коэффицентов в системе уравнений метода наименьших квадратов
    sx = sum(x)
    stime = sum(time)
    sx2 = sum(i**2 for i in x)
    sxtime = sum(i*j for i, j in zip(x, time))
    n = len(x)
    # k - это коэффициент, при котором вычитание
    # из первого уравнения второго,
    # умноженного на него, приводит к нулю в коэффициенте при x.
    # Таким образом, мы сможем вычислить свободный коэффициент.
    k = sx2/sx
    # bur - это свободный коэффицент
    bur = (sxtime - k*stime)/(sx-k*n)
    # aur - это коэффицент при x
    aur = (stime - bur*n)/sx
    # Создание графических окон
    plt.figure(namegraph)
    # Создание графиков
    correlation_v.append(create_graph(x, time, aur, bur))

print("Коэффициент корреляции в первом случае =",
      correlation_v[0], "\nа во втором случае =", correlation_v[1])

# Показ графиков
plt.show()
