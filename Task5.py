# Реализуйте алгоритм перемешивания списка.

import os
os.system("cls")
from random import randint

def MixList(list_in):
    mix_list = list_in[:]
    for i in range(len(mix_list)):
        index_rand = randint(0, len(mix_list) - 1)
        temp = mix_list[i]
        mix_list[i] = mix_list[index_rand]
        mix_list[index_rand] = temp
    return mix_list

n = int(input("Введите N = "))

list_n = [i for i in range(1, n+1)]    # создаем список от 1 до N
print('\n')
print("Исходный список: ")
print(list_n)
print("Перемешанный список: ")
print(MixList(list_n))
print('\n')

