def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = [2.2, True, [1, 2, 3]]
values_dict = {'a': 74, 'b': "Ангарск", 'c': 6.5}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)





