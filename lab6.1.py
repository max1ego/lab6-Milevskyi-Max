import math

def f(x):
    return math.cos(x) / (1 + abs(math.sin(x)))

print("Введіть діапазон і крок: ")

print("Початок діапазону: ")
start = float(input())
print("Кінець діапазону: ")
end = float(input())
print("Крок: ")
step = float(input())

iterationNum = int(abs(end - start) / step) + 1

listFor = []
for i in range(iterationNum): 
    inputVal = i * step + start
    listFor.append(f(inputVal))

listWhile = []
while start <= end:
    listWhile.append(f(start))
    start += step

print(*listFor, sep="\n")

maxValue = max(listFor)
minValue = min(listFor)

betweenValues = []
minIndex = listFor.index(minValue)
maxIndex = listFor.index(maxValue)

for i in range(min(minIndex, maxIndex) + 1, max(maxIndex, minIndex)): 
    betweenValues.append(listFor[i])

print("Елементи між найбільшим і найменшим:")
print(*betweenValues, sep="\n")