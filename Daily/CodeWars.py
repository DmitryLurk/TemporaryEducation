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
