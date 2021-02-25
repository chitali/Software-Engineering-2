def fib(num):
    try:
        num = int(num)
    except:
        return "Error"
    if num == 0:
        return 0
    elif num <= 2:
        return 1
    answer = [1,1]
    for i in range(2,num):
        answer.append(answer[i-1] +answer[i-2])
    return answer[-1]

