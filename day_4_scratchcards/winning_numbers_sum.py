matches = [
    len(set(line[: line.find("|")].split()) & set(line[line.find("|") + 1 :].split()))
    for line in open("day_4_scratchcards/data.txt")
]

cards = [1] * len(matches)
for i, n in enumerate(matches):
    for j in range(n):
        cards[i + j + 1] += cards[i]

print(sum(2 ** (n - 1) for n in matches if n > 0))
print(sum(cards))
