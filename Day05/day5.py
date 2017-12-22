def jumps1(lst):
    i = 0
    cur = 0
    while cur < len(lst):
        lst[cur], cur = lst[cur]+1, cur + lst[cur]
        i += 1
    return i

def jumps2(lst):
    def offset(val):
        if val >= 3:
            return -1
        return 1
    i = 0
    cur = 0
    while cur < len(lst) and cur >= 0:
        if lst[cur] >= 3:
            lst[cur] -= 1
            cur += lst[cur] + 1
        else:
            lst[cur] += 1
            cur += lst[cur] - 1
        i += 1
#        print(lst, cur)
#    print(lst)
    return i

if __name__ == "__main__":
    f = open("input.txt")
    inpt = list(map(lambda x: int(x), f.read().strip().split('\n')))
    f.close()
    print(jumps1(inpt))
    print(jumps2(inpt))
    print(jumps2([0, 3, 0, 1, -3]))
