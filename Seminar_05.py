def even(i):
    return i % 2 == 0

some_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(some_list) # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
some_list = list(map(int, some_list))
print(some_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
some_list2 = list(filter(even, some_list))
print(some_list2) # [2, 4, 6, 8, 10]
new_list = list(filter(lambda i: i % 2 == 0, some_list))
print(new_list) # [2, 4, 6, 8, 10]
new_list2 = list(map(lambda x: x ** 3, [1, 2, 3, 4, 5]))
print(new_list2) # [1, 8, 27, 64, 125]
new_list3 = list(filter(lambda x: x ** 3, [1, 2, 3, 4, 5]))
print(new_list3) # [1, 2, 3, 4, 5]

num_list = [1, 2, 3, 4, 5]
user_list = ['one', 'two', 'three', 'four', 'five']
all_list = list(zip(num_list, user_list))
print(all_list) # [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')] - лист
all2_list = {} # словарь
for i, j in zip(num_list, user_list): # можно zip менять на filter, map - так как это итераторы
    all2_list[j] = i
print(all2_list) # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
u = {'first', 'second', 'third', 'four', 'five'}
i = {1, 2, 3}
test = {'one', 'two', 'three'}
a = {}
for i, j, k in zip(u, i, test):
    a[j] = i, k
    # a[j] = k
print(a) # {1: ('third', 'two'), 2: ('five', 'one'), 3: ('second', 'three')}
print(a[1]) # ('third', 'one')
print(a[1][1])

u = ('first', 'second', 'third', 'four', 'five')
i = (1, 2, 3)
test = ('one', 'two', 'three')
a = {}
for i, j, k in zip(u, i, test):
    a[j] = i, k
    # a[j] = k
print(a) # {1: ('first', 'one'), 2: ('second', 'two'), 3: ('third', 'three')}
print(a[1]) # ('first', 'one')
print(a[1][1]) # one

some_list = [8, 89, 213, 45, 74, 2, 3]
print(list(enumerate(some_list))) # [(0, 8), (1, 89), (2, 213), (3, 45), (4, 74), (5, 2), (6, 3)] - выведет "идекс - элемент"

a_list = [i ** 2 for i in range(1, 11) if not i % 2]
b_list = [x ** 2 for x in range(1, 11) if not x % 2 == 0]
print(list(enumerate(a_list)))
print(list(enumerate(b_list)))

def f(my_list: list) -> int:
    '''find max element''' # так можно оставлять описание
    return max(my_list)
any_list = [154, 546, 51, 879, 54]
print(f(any_list))
print(type(f(any_list))) #  <class 'int'>
print(type(max(any_list))) #  <class 'int'>

# Задачи: =============================================================================================================================

# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.

# 2. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# Задача 1: ===========================================================================================================================
with open('task01.txt', 'r') as file:
    some_str = file.readline()
some_list = list(map(int, some_str.split()))
print(some_list)
for i in range(1, len(some_list)):
    if some_list[i] - 1 != some_list[i - 1]:
        print(some_list[i] - 1)
# Задача 2: ===========================================================================================================================
my_text = 'абв бльыд лотсшы сбзцс абв адль бв сла зцщу ждазцщ зцщл Альдь'
my_text_list = list(filter(lambda i: 'абв' not in i and 'а' not in i and 'б' not in i and 'в' not in i, my_text.split()))
print(my_text_list)
