def valid(phrase):
    """ Checks if passphrase only contains distinct
    words.
    >>> valid('aa bb cc dd')
    True
    >>> valid('aa bb aa')
    False
    >>> valid('aa bb aaa')
    True
    """
    words = []
    series_of_words = phrase.split(' ')
    words.append(series_of_words.pop())
    for word in series_of_words:
        if word in words:
            return False
        words.append(word)
    return True

if __name__ == "__main__":
    f = open("input.txt")
    inpt = f.read().strip()
    f.close()
    total = 0
    phrases = inpt.split('\n')
    print(len(phrases))
    for phrase in phrases:
        if valid(phrase):
            total += 1
    print(total)
