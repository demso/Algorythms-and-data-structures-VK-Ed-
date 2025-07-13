#В первой строке задаётся число  N  — размер массива (количество элементов).
#Во второй строке вводится массив из  N  чисел, разделённых пробелами.
#В третьей строке задаётся число element, которое нужно удалить из массива.
#На выходе программа должна вывести строку из элементов массива, из которого удалены все вхождения числа element. 
#Оставшиеся числа должны быть записаны через пробел.

right = 0

def do_work(li, element):
    global right
    right = len(li)-1
    i = 0
    while i < right:
        if li[i] == element:
            for j in range(i, right):
                li[j] = li[j+1]
            li[right] = element
            right-=1
            continue
        i+=1    

size = int(input())
list = list(map(int, input().split()))
element = int(input())

do_work(list, element)

print(*list[:right+1], sep = " ")
    
#1 2 5 -1 -1 5 8 -1 8 9.6 8.5 -1 0

