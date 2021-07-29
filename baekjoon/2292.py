N = int(input())
i, _min, _max = 0, 1, 1
while True:
    if _min <= N and N <= _max:
        print(i+1)
        break
    i += 1
    _min = _max + 1
    _max = _max + i*6