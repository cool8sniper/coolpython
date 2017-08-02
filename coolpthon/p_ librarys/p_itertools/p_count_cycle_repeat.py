from itertools import count, repeat, cycle

for i in zip(count(1), ['a', 'b', 'c']):
    print(i, end=' ')

print("\n================Test cycle===============")
for i in zip(range(6), cycle(['a', 'b', 'c'])):
    print(i, end=' ')


print("\n================Test repeat===============")
for i, s in zip(count(1), repeat('over-and-over', 5)):
    print(i, s)
print("\n")
