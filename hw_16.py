
while True:
    user_string = input('enter number').split()
    try:
        int(user_string[1])!= 0
    except (TypeError,ValueError):
        print('для деления нужны цифры')
    except IndexError:
        print('введите числа')

    else:
            try:
                res = int(user_string[0])/int(user_string[1])
            except ValueError:
                print('Для деления нужны цифры 2')
            except IndexError:
                print('нужно не меньше двух чисел')
            except ZeroDivisionError:
                print('Введите заново числа')
            except NameError:
                res = 0
                print(res)
            else:
                print(res)

