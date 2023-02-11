from collections import defaultdict

word = list(map(str, input().upper()))
word_dict = defaultdict(int)

for w in word:
    word_dict[w] += 1

rank = [(key, value) for key, value in word_dict.items()]
rank = sorted(rank, key= lambda x: x[1])

if len(rank) > 1 and rank[-1][1] == rank[-2][1]:
    print('?')
else:
    print(rank[-1][0])