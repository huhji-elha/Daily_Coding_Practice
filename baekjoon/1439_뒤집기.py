import sys
s = list(sys.stdin.readline())[:-1]

if len(set(s)) == 1:
    print(0)
else:
    passed = s[0]
    count_dict = {"0": 0, "1": 0}
    count_dict[passed] += 1
    for i in s[1:]:
        if i != passed:
            count_dict[i] += 1
            passed = i
    print(min(count_dict["0"], count_dict["1"]))
