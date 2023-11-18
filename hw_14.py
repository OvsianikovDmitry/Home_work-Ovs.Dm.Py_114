mas = ['weew',4,'fsfdd',5,8,12,'ff','qwe',9,'ertyuu']
list_num = []
list_word =[]

for i in mas:
    i = str(i)
    if i.isdigit():
        list_num.append(i)
    elif i.isalpha():
        list_word.append(i)

list_word.sort(key=len)
list_num.sort(key = int)

with open('dz.txt','w') as f:
    for i in list_word:
        f.write(i + ' ')
    for i in list_num:
        f.write(i + ' ')