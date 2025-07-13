#Дан отсортированный по возрастанию массив целых чисел и заданное число. Если заданное число уже находится в массиве, верните его индекс. 
#Если числа в массиве нет, верните индекс, где оно должно находиться, чтобы сохранить порядок сортировки.



def do_work(li, target):
    left = 0
    right = len(li)-1
    answer = None
    
    while left <= right:
        middle = int(left + (right - left)/2)
        if target == li[middle]:
            answer = middle
            break
        elif target > li[middle]:
            left = middle+1
        elif target < li[middle]:
            right = middle-1
     
    if answer == None:
        answer = left   
    
    print(answer)


size = int(input())
list = list(map(int, input().split()))
target = int(input())
do_work(list, target)


