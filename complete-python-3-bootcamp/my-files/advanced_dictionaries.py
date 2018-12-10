d1 = {'k1': 1, 'k2': 2}
print(d1)

# Dictionary comprehensions
d2 = {k: v**2 for k, v in zip(['a', 'b', 'c', 'd'], range(4))}
print(d2)

for k in d1.keys():
    print(k)
