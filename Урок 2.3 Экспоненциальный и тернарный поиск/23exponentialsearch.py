#реализация экспоненциального поиска для вычисления диапазона, в котором находится значение target

def do_work(li, target):
    left = 0
    right = len(li) - 1
    found = False
    border = 1
    while not found:
        if li[border - 1] >= target:
            left = int(border/2)
            right = border
            found = True
        elif li[border - 1] < target:
            border *= 2
    print(left, right)

size = int(input())
list = list(map(int, input().split()))
target = int(input())
do_work(list, target)
    


