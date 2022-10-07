def duplicate_count(text):
    text = text.lower()
    p = 0
    m = set(text.lower())
    for i in m:
        if text.count(i) > 1:
            p += 1
    print(m)
    print(text)
    return print(p)


duplicate_count("kgBilXIrPjdO60tdsK9ZKl7q81lguMbNtrcBakWJ06WI7pZ02LZEm6WPfx")
