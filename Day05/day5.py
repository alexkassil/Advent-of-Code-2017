def jumps(lst):
    i = 0
    cur = 0
    while cur < len(lst):
        lst[cur], cur = lst[cur]+1, cur + lst[cur]
        i += 1
    return i

if __name__ == "__main__":
    f = open("input.txt")
    inpt = list(map(lambda x: int(x), f.read().strip().split('\n')))
    f.close()
    print(jumps(inpt))
