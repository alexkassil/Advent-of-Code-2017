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

def valid_anagram(phrase):
    """ Checks if passphrase only contains 
    words that aren't anagrams of each other.
    >>> valid_anagram('abcde fghij')
    True
    >>> valid_anagram('abcde xyz ecdab')
    False
    >>> valid_anagram('a ab abc abd abf abj')
    True
    >>> valid_anagram('iiii oiii ooii oooi oooo')
    True
    >>> valid_anagram('oiii ioii iioi iiio')
    False
    """
    words = []
    series_of_words = phrase.split(' ')
    words.append(''.join(sorted(series_of_words.pop())))
    for word in series_of_words:
        word = ''.join(sorted(word))
        if word in words:
            return False
        words.append(word)
    return True

if __name__ == "__main__":
    f = open("input.txt")
    inpt = f.read().strip()
    f.close()
    total1 = 0
    total2 = 0
    phrases = inpt.split('\n')
    print(len(phrases))
    for phrase in phrases:
        if valid(phrase):
            total1 += 1
        if valid_anagram(phrase):
            total2 += 1
    print(total1, total2)
