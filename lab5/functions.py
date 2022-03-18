from Point import Point
import random
import matplotlib.pyplot as plt
from math import *
from Vector import Vector

def initPoints(n) -> list:
    X = [random.randint(0, 10) for _ in range(n)]
    Y = [random.randint(0, 10) for _ in range(n)]
    points = []
    for i in range(len(X)):
        el = Point(X[i], Y[i])
        for j in range(len(points)):
            if el.equals(points[j]):
                el.x = random.randint(0, 10)
                el.y = random.randint(0, 10)
        points.append(el)
    return points

def determinant(p, p1, p2):  # p относительно p1p2
    return (p2.x - p1.x) * (p.y - p1.y) - (p.x - p1.x) * (p2.y - p1.y)

def drawPolygon(points: list):
    for i in range(0, len(points)):
      if i + 1 == len(points):
        k = 0  # k - индекс последней точки
      else:
        k = i + 1
      plt.plot([points[i].x, points[k].x], [points[i].y, points[k].y], color="orange")

def drawPoints(points):
    n = len(points)
    for i in range(n):
        plt.scatter(points[i].x, points[i].y)  # рисует точку

def area(p1,p2,p3):
    return abs(determinant(p3, p1, p2))

def distance(p1, p2):
    return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2))

def findMinPoint(points, S):
    n = len(points)
    for i in range(1, n):
        if points[S[i]].y < points[S[0]].y:
            S[i], S[0] = S[0], S[i]  # меняем местами номера этих точек
    for i in range(1, n):
        if points[S[i]].y == points[S[0]].y:
            if points[S[i]].x < points[S[0]].x:
                S[i], S[0] = S[0], S[i]

def jarvis(points):
    n = len(points)
    S = list(range(0, n))  # список номеров точек
    findMinPoint(points, S)      # start point

    H = [S[0]]  # список для хранения вершин в нужном порядке
    del S[0]
    S.append(H[0])  # заносим стартовую вершину в конец
    hull = []
    while True:
        right = 0
        for i in range(1, len(S)):
            if determinant(points[S[i]], points[H[-1]], points[S[right]]) < 0:
                right = i
        if S[right] == H[0]:
            break
        else:
            H.append(S[right])
        del S[right]

    for i in range(0, len(H)):
        hull.append(points[H[i]])

    return hull


def findDiameter(points):
    k = len(points)
    i = 1
    d = 0

    while area(points[k-1], points[0], points[i]) < area(points[k-1], points[0], points[i + 1]):
        i += 1
    start = i

    j = 0
    while start < k:
        tmp = start
        while area(points[j % k], points[(j + 1) % k], points[tmp % k]) <= area(points[j % k], points[(j + 1) % k], points[(tmp + 1) % k]):
            tmp += 1
        end = tmp

        for l in range(start, end + 1):
            if distance(points[j % k], points[l % k]) > d:
                tmp1 = points[j % k]
                tmp2 = points[l % k]
                d = distance(points[j % k], points[l % k])

        start = end
        j += 1
    res = {'distance': d, 'points': [tmp1, tmp2]}
    return res

def mainTask(points):
    plt.ion()  # включение интерактивного режима для анимации

    time = 30
    hull = jarvis(points)
    MAX_D = findDiameter(hull)['distance']

    while time:
        plt.clf()  # очистить текущую фигуру
        drawPoints(points)
        hull = jarvis(points)
        drawPolygon(hull)
        d = findDiameter(hull)['distance']
        oppPoints = findDiameter(hull)['points']
        if d > MAX_D:
            for p in oppPoints:
                scalar = -1
                tmpVector = Vector.multiplyOnScalar(p.direction, scalar)
                p.setDirection(tmpVector)
        for p in points:
            p.next()  # точка движется дальше по направлению

        plt.draw()
        plt.gcf().canvas.flush_events()
        plt.pause(0.000001)
        time -= 1

    plt.ioff()  # выключение интерактивного режима
    plt.show()