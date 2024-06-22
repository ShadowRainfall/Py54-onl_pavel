def func():
    f = False
    res = list[int(f), int(not f), int(str(int(not f)) + str(int(f)))]
    return res
print(func())