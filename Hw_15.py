import json


# #задача 1 вар1
# str = ''
# name = []
# price =[]
# user_str = {}
# while str != 'stop':
#     name.append(input('Покупка'))
#     price.append(input('Стоимость'))
#     str = input(f'"stop" - закончить", "enter" - продолжить ')
#
# user_str['Покупка'] = name
# user_str['Стоимость'] = price
#
# with open('user_list.json', 'w', encoding='utf-8') as f:
#     json.dump(user_str,f,ensure_ascii=False)

# задача2 вар1

with open('user_list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
summa = 0
price = data.setdefault('Стоимость')
for i in price:
    summa += int(i)
print(summa)


#задача 1 вар2
# str = ''
# user_dict = {}
# while str != 'stop':
#     user_dict[input('Название')] = input('Стоимость')
#     str = input(f'"stop" - закончить"')
#
# with open('user_list_2.json', 'w', encoding='utf-8') as f:
#     json.dump(user_dict,f,ensure_ascii=False)


#задача2 вар2

with open('user_list_2.json', encoding='utf-8') as f:
    new_file = json.load(f)

summa = 0
for k,v in new_file.items():
    summa += int(new_file[k])

print(f'стоимость всех покупок {summa}')