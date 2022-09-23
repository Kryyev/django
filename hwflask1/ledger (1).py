lst = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

numbers = [10, 15, 21, 33, 42, 55]


lst_map = list(map(lambda data: (data[0], round(data[2] * data[3] + 10 if data[2] * data[3] < 100 else data[2] * data[3], 2)), lst))

print(lst_map)