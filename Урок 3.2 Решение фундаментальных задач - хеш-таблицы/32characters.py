#найти элемент, который встречается болле половины раз или вывести -1 с использованием хеш-таблиц

def do_work(li):
    answer = -1
    char_table = dict()
    for x in li:
        if x in char_table:
            char_table[x] += 1
        else:
            char_table[x] = 1
        list_length = len(li)
    for x in iter(char_table):
        if char_table[x] > int(list_length/2):
            answer = x
            break
    print(answer)

size = int(input())
list = list(map(int, input().split()))
do_work(list)
    


