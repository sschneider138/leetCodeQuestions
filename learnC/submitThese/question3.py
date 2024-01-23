

dict = {
    2: "alice",
    4: "bob",
    12: "eve"
}

def func(x, map):
    for i in range(1, x + 1):
        tmp = ""
        for num in map:
            if i % num == 0:
                tmp += map[num] + ", "
        if tmp:
            print(i, tmp)
        else:
            print(i)


# test case:      
# a = func(12, dict)