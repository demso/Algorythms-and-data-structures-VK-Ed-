#В первой строке задаётся число N — размер массива (количество оценок). 
#Во второй строке вводится массив из N целых чисел, разделённых пробелами.
#Программа должна вывести строку из N элементов массива, где все нули перемещены в конец, 
#а порядок остальных чисел сохранён. Значения разделяются пробелами.

import random

def sort(li):
    right = len(li)-1
    i = 0
    while i < right:
        if li[i] == 0:
            for j in range(i, right):
                li[j] = li[j+1]
            li[right] = 0
            right-=1
            continue
        i+=1

size = int(input())
list = list(map(int, input().split()))
sort(list)
print(*list, sep = " ")
    


