str = "This guide is hello hello hello hello specifically for contributing to the Python reference interpreter, also known as CPython (while most of the standard library is written in Python, ethe interpreter core is written in C and integrates most easily with the C and C++ ecosystems)"





def max_word(string):
    lst = string.split(' ')
    dictionary = {}

    for i in range(len(lst)):
        if lst[i] in dictionary:
            dictionary[lst[i]] += 1
        else:
            dictionary[lst[i]] = 1

    count = 0
    word = ''
    for w in dictionary:
        if dictionary[w] >= count:
            word = w
            count = dictionary[w]

    print(word)


max_word(str)