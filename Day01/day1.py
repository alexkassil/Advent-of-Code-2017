def inverse_captcha(inpt):
    """ Takes in a sequence of digits and returns
    the sum of all digits that match the next digit
    in the list. The list is circular, so digit after 
    last is first.
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

def inverse_captcha_halfway(inpt):
    """ Takes in a sequence of digits and returns
    the sum of all digits that match the digit that is
    halfawy around the list. The lenght of each list is
    even, with the first entry matching with the n/2th
    entry, where n is the end of the list.
    >>> inverse_captcha_halfway('1212')
    6
    >>> inverse_captcha_halfway('1221')
    0
    """
    result = 0
    lst = list(inpt)
    n = len(lst)
    for i in range(len(lst)):
        if lst[i] == lst[i-(n//2)]:
            result += int(lst[i])
    return result

if __name__ == "__main__":
    f = open("input.txt")
    inpt = f.read().strip()
    f.close()
    print(inverse_captcha(inpt))    
    print(inverse_captcha_halfway(inpt))    
