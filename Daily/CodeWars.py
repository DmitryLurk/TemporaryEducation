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
        return f'{names[0]}, {names[1]} and {len(names)-2} others like this'
likes(['Max', 'John', 'Mark'])