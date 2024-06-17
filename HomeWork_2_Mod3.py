def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [500, 'Привет!', True]
values_list_2 = [54.32, 'Строка']
values_dict = {'a': 2.258, 'b': False, 'c': 'Словарь'}
print_params(*values_list)
print_params(*values_list_2, 42)
print_params(**values_dict)
