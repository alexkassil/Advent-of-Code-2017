def checksum(inpt):
    """Return the sum of the differences between
    the smallest and largest entry in each row
    >>> checksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]])
    18
    """
    result = 0
    for row in inpt:
        result += max(row) - min(row)
    return result
        
def checksum_divisible(inpt):
    """Return the sum of the largest quotients in
    each row that are a whole number
    >>> checksum_divisible([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]])
    9
    """
    result = 0
    for row in inpt:
        result += max(quotients(row))
    return result

def quotients(row):
    """Returns an array of quotients for each entry
    divided by every other entry if evenly divisible.
    >>> sorted(quotients([3, 2, 9, 8]))
    [1, 1, 1, 1, 3, 4]
    """
    result = []
    for entry in row:
        result.extend(map(lambda x: x//entry, filter(lambda x: x%entry == 0, row)))
    return result

if __name__ == "__main__":
    f = open('input.txt')
    inpt = f.read().strip()
    f.close()
    inpt_lst = [[int(e) for e in t.split('\t')] for t in inpt.split('\n')]
    print(checksum_divisible(inpt_lst))

