import random as rnd
from statistics import correlation
import matplotlib.pyplot as plt
import numpy as np
import timeit


def findmin(a, maxitem, len):
    min = maxitem
    for i in range(len):
        if min > a[i]:
            min = a[i]
    return min

def findmax(a, len):
    max = 0
    for i in range(len):
        if max < a[i]:
            max = a[i]
    return max


def create_graph(b, c, aur, bur):
    y_values = np.linspace(0, max(c), num=5)
    x_values = np.linspace(0, b[-1], num=11)
    plt.scatter(b, c, s=5)

    y_line = aur * np.array(b) + bur
    plt.plot(b, y_line, color='red')
    plt.title("График")
    plt.xlabel("X-ось")
    plt.ylabel("Y-ось")
    plt.xticks(x_values)
    plt.yticks(y_values)
    correlation_coefficient = np.corrcoef(c, b)[0, 1]
    return correlation_coefficient


correlation_v = []
# Цикл нужен для создания двух графиков, один при среднем случае, второй при худшем
for namegraph in ["Минимум", "Максимум"]:
    x = []
    time = []
    x2 = []
    xtime = []
    randmax = 1000000
    for i in range(10, 10001, 10):
        x.append(i)
        a = [rnd.randint(0, randmax) for j in range(i)]
        if namegraph == "Минимум":
            timer = timeit.timeit(lambda: findmin(a, randmax, i), number=1)
        else:
            timer = timeit.timeit(lambda: findmin(a, randmax, i), number=1)
        time.append(timer)

    for i, j in zip(x, time):
        x2.append(i**2)
        xtime.append(i*j)
    # Вычисление коэффицентов в системе уравнений метода наименьших квадратов
    sx = sum(x)
    stime = sum(time)
    sx2 = sum(x2)
    sxtime = sum(xtime)
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
