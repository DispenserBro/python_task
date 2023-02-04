# from random import randint

#* Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции

def sum_on_odd_pos(lst: list) -> int | float:
    return sum(lst[1::2])


# number_els = int(input('Enter the number of elements: '))
# Если хочется вводить ручками)

# lst_in = []

# for i in range(number_els):
#     lst_in.append(int(input(f'Enter the {i+1} element: ')))
#     lst_in.append(float(input(f'Enter the {i+1} element: ')))


# Если не хочется вводить ручками))))

# max_number = int(input('Enter the max number: '))

# lst_in = [randint(0, max_number) for _ in range(number_els)]


# Примеры с сайта
lst_in = [
    [2, 3, 5, 9, 3], # -> 12
    [1, 2, 3, 4, 5], # -> 6
    [10, 11, 15, 24] # -> 35
        ]

for el in lst_in:
    print('Full list:', el, sep='\n')

    sum_result = sum_on_odd_pos(el)
    print(f'Sum of elements on odd positions: {sum_result}')

print('That\'s all, folks!' )
