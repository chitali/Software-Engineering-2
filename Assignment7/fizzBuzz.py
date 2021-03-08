def fb():
    arr = []
    for x in range(1, 101):
        if x % 3 == 0:
            arr.append('Fizz')
        elif x % 5 ==0:
            arr.append('Buzz')
        else:
            arr.append(x)
    return arr