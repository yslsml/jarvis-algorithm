# Задание
Дано:
Пусть D некоторая заданная константа и P = {p1(x1, y1), p2(x2, y2), … ,pn(xn, yn)} –
произвольное множество точек на плоскости.
Необходимо реализовать анимацию, в которой точки движутся с
постоянными скоростями и направлениями. Как только расстояние между
двумя точками становиться больше чем D эти две точки меняют свои
скорости на противоположные.
Примечания: На каждом шаге анимации необходимо находить две самые
удаленные точки, используя алгоритм отыскания “диаметра множества”.
Первым шагом этого алгоритма является построение выпуклой оболочки,
которое необходимо реализовать “алгоритмом Джарвиса”. 

# Task
Given:
Let D be some given constant and P = {p1(x1, y1), p2(x2, y2), ... ,pn(xn, yn)} be
an arbitrary set of points on the plane.
It is necessary to implement an animation in which the points move with
constant speeds and directions. As soon as the distance between
two points becomes greater than D, these two points change their
speeds to opposite ones.
Notes: At each step of the animation, it is necessary to find the two most
distant points using the algorithm for finding the "diameter of the set".
The first step of this algorithm is to construct a convex hull,
which must be implemented by the "Jarvis algorithm".
