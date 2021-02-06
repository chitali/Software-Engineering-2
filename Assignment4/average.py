def calcAvr(arr):
    if len(arr) <= 0:
        return "Error"
    for index, x in enumerate(arr):
        try:
            arr[index] = float(x)
        except ValueError:
            return "Error"
    return sum(arr) / len(arr)
