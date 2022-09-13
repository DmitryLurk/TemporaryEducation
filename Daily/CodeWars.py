def high(x):
    dict_kwargs = {}
    d = []
    dict_vals = 1
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower():
        dict_kwargs[i] = dict_vals
        dict_vals += 1
    print(dict_kwargs)
    for words in x.split(' '):
        p = 0
        for i in words:
            p += dict_kwargs[i]
        d.append(p)
    return print(x.split(' ')[d.index(max(d))])


high('take me to semynak')


def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


likes(['Max', 'John', 'Mark'])


def square_digits(num):
    '''square every digit of a number and concatenate them.
    For example, if we run 9119 through the function, 811181
    will come out, because 92 is 81 and 12 is 1.'''
    return print(int(''.join(str(pow(int(i), 2)) for i in str(num))))


square_digits(9119)


def basic_op(operator, value1, value2):
    return print(eval(f'{value1} {operator} {value2}'))


basic_op('+', 4, 7)
