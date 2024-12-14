data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def sum(arg):
    total = 0
    if isinstance(arg, (int, float)):
        total += arg
    elif isinstance(arg, str):
        total += len(arg)
    elif isinstance(arg, (list, tuple, set)):
        for element in arg:
            total += sum(element)
    elif isinstance(arg, dict):
        for key, value in arg.items():
            total = total + sum(value) + sum(key)
    return total


result = sum(data_structure)
print('Cумма всех чисел и длин всех строк:',result)
