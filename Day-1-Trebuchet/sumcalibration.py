data = open("Day-1-Trebuchet/data.txt")
sum = 0
digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def indices(n, w, start=0):
    index = n.find(w, start)
    if index == -1:
        return []
    return [index] + indices(n, w, index + 1)


def append_indices(foundnum, indices, word, number):
    if indices:
        # print(indices, word, number + 1)
        for j in indices:
            foundnum.update({j: number + 1})


for x in data:
    # print(x)
    foundnum = {}
    for idx, word in enumerate(digits):
        i = indices(x, word)
        n = indices(x, str(idx + 1))
        append_indices(foundnum, i, word, idx)
        append_indices(foundnum, n, word, idx)
    ha = list(foundnum.keys())
    ha.sort()
    num = int("{}{}".format(foundnum.get(ha[0]), foundnum.get(ha[-1])))
    # print(num)
    sum += num
print(sum)


data.close()
