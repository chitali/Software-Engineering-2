def fb(i):
    arr = []
    for x in range(1, 101):
        if x % 3 == 0:
            arr.append('Fizz')
        else:
            arr.append(x)
    return arr