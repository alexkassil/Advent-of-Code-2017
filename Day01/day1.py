def inverse_captcha(inpt):
    """ Takes in a sequence of digits and returns
    the sum of all digits that match the next digit
    in the list. The list is circular, so digit after 
    last is first
    >>> inverse_captcha('1122')
    3
    >>> inverse_captcha('1111')
    4
    """
    result = 0
    lst = list(inpt)
    for i in range(len(lst)):
        if lst[i] == lst[i-1]:
            result += int(lst[i])
    return result

if __name__ == "__main__":
    f = open("input.txt")
    print(f.read())
