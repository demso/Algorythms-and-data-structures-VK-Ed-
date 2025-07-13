#реализация быстрой сортировки, сортировка массива

def quick_sort(li):
    mid = int(len(li) / 2)
    bigger = []
    smaller = []
    if len(li) >= 3:
        mid_value = li[mid]
        for i in range(len(li)):
            n = li[i]
            if i == mid:
                continue
            if n > mid_value:
                bigger.append(n)
            elif n <= mid_value:
                smaller.append(n)
        sorted_bigger = quick_sort(bigger)
        sorted_smaller = quick_sort(smaller)
        whole_list = sorted_smaller + [mid_value] + sorted_bigger
        return whole_list
    elif len(li) >= 2:
        if li[0] > li [1]:
            li[0], li[1] = li[1], li[0]
        return li
    else:
        return li

size = int(input())
list = list(map(int, input().split()))
list = quick_sort(list)
print(*list, sep = " ")
    


