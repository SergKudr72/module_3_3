def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(2, 3, 4)
print_params(4, 'ёж')
print_params(8)

print_params(b=25)
print_params(c=[1,2,3])

values_list = [7, 'cinema', False]
values_dict = {'a': 9, 'b': 'day', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)
