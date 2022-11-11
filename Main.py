import numpy
import matplotlib.pyplot

N = int(input("Номер элемента ряда Фибоначчи: "))

Mas = []

i = 0
for i in range(N):
if (i==0): Mas.append(1)
if (i==1): Mas.append(1)
if (i>1): Mas.append(Mas[i-1] + Mas[i-2])
print(Mas)
Y = []
for i in range(N): Y.append(i)
matplotlib.pyplot.plot(Y, Mas)
matplotlib.pyplot.show()