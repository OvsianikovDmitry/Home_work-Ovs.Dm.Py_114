def debug(func):
    def wrapper(*args,**kwargs):
        print(f'Это функция: {func.__name__}, и у неё есть аргументы {args},{kwargs}')
        return print(f'{func.__name__} возвращает значение {func(*args,**kwargs)}')
    return wrapper


@ debug
def example(*args):
    a = sum(args)
    return a



example(3,5,54,3)