# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
n = int(input('Введите длину списка'))
rand_int = [random.randint(-10,10) for _ in range(n)]
new_list = []
new_list=[i**2 for i in rand_int]
print(str(rand_int)+'-->'+str(new_list))


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits1 = ['lemon', 'mango', 'lychee', 'guava']
fruits2 = ['papaya', 'lychee', 'guava', 'orange', 'grapefruit']
res_list = list(set(fruits1) & set(fruits2))
print('Совпадающие элементы', res_list)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
init = [random.randint(-10, 10) for _ in range(10)]
multiple_of_three = [i for i in init if i%3==0]
is_positive = [i for i in init if i>0]
not_multiple_of_four = [i for i in init if i%4!=0 ]
print('Исходоный список: ', init)
print('Кратны трем: ', multiple_of_three)
print('Положительные:', is_positive)
print('Не кратны 4:', not_multiple_of_four)



