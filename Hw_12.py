def what_is(x):
    if type(x) is tuple:
        count = 0
        for i in str(x):
            if i.isalpha():
                count += len(i)
        return print(f'длина всех слов: {count}')
    elif type(x) is list:
        amount_number = 0
        amount_letter = 0
        for i in str(x):
            if i.isalpha():
                amount_letter += 1
            elif i.isdigit():
                amount_number += 1
        return print(f'Количество букв: {amount_letter}, Количество чисел: {amount_number}')
    elif type(x) is int:
        number = str(x)
        count = 0
        for i in number:
            if int(i) % 2 != 0:
                count += 1
        return print(f'Количество нечётных цифр: {count}')
    elif type(x) is str:
        amount_letter = 0
        for i in x:
            if i.isdigit():
                continue
            elif i.isalpha():
                amount_letter += 1
        return print(f'Количество букв в строке: {amount_letter}')


tup = ('dsf', 2, 'fsf', 5, 6, 7, 8)
l_1 = ['dsf', 2, 'fsf', 5, 6, 7, 8]
number = 123445
stringa = 'gdsgarhsj125'
what_is(stringa)
