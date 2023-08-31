from itertools import combinations
result = []
my_wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
for i in range(1, len(my_wallet)+1):
    for y in combinations(my_wallet, i):
        if sum(y) == 100:
            result.append(y)

print(set(result))
print(len(set(result)))
