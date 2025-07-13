#В первой строке задаётся число N — размер массива (количество элементов).
#Во второй строке вводится массив из N положительных целых чисел, разделённых пробелами.
#В первой строке задаётся число N — размер массива (количество элементов).
#Во второй строке вводится массив из N положительных целых чисел, разделённых пробелами.

def do_work(li):
    first = li[0]
    second = li[1]
    min_sum = abs(li[1] - li[0])
    for x in range(2, len(li)):
        cur_sum = abs(li[x] - li[x-1])
        if cur_sum < min_sum:
            min_sum = cur_sum
            first = li[x-1]
            second = li[x]
    print(first, second)

size = int(input())
list = list(map(int, input().split()))
do_work(list)
    


