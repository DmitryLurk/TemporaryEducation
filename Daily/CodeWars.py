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


def expanded_form(num):
    num = str(num)
    counter = len(num)
    result = ''
    for i in num:
        counter -= 1
        if i not in '0':
            if counter < 0:
                counter = 0
            result += str(int(i) * (10 ** counter))
            if counter != 0:
                result += ' + '
    return print(result[:-3]) if result[-3:] == ' + ' else print(result)


expanded_form(9000000)
expanded_form(70304)


def is_valid_walk(walk):
    """You always walk only a single block for each letter (direction)
    and you know it takes you one minute to traverse one city block,
    so create a function that will return true
    if the walk the app gives you will take you exactly ten minutes
    (you don't want to be early or late!) and will, of course, return you to your starting point.
    Return false otherwise."""
    if len(walk) != 10:
        return print(False)
    os_x = 0
    os_y = 0
    for i in walk:
        if i == 'n':
            os_x += 1
        elif i == 's':
            os_x -= 1
        elif i == 'e':
            os_y += 1
        elif i == 'w':
            os_y -= 1
    return print(True) if os_x == 0 and os_y == 0 else print(False)


is_valid_walk(['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's'])


def divisors(n):
    """Count the number of divisors of a positive integer n."""
    count = 0
    i = n
    if n != 1:
        while i != 0:
            if i == 0:
                return print(count)
            if n % i == 0:
                count += 1
                i -= 1
            else:
                i -= 1
        return print(count)
    else:
        return print(1)


def sum_array(arr):
    """Sum all the numbers of a given array ( cq. list ),
except the highest and the lowest element ( by value, not by index! ).
The highest or lowest element respectively is a single element at each
edge, even if there are more than one with the same value."""
    if arr == None or len(arr) == 0 or len(arr) == 1:
        return 0
    return sum(arr) - max(arr) - min(arr)


def correct(s):
    """Your task is correct the errors in the digitised text. """
    result = s
    mist = {5: "S", 0: "O", 1: "I"}
    for i in result:
        try:
            result = result.replace(i, mist[int(i)])
        except Exception:
            pass
    return print(result)
