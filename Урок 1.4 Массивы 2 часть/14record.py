#В первой строке задаётся число N — размер массива (количество результатов).
#Во второй строке вводится массив из N целых чисел, разделённых пробелами.
#Программа должна вывести одно число — максимальное значение из массива.

def do_work(li):
    record = 0
    for n in li:
        if n > record:
            record = n
    return record

size = int(input())
list = list(map(int, input().split()))
print(do_work(list))
    


