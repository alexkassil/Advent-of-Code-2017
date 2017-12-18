def checksum(inpt):
    """Return the sum of the differences between
    the smallest and largest entry in each row"""
    result = 0
    for row in inpt:
        result += max(row) - min(row)
    return result
        

if __name__ == "__main__":
    print(checksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]))
