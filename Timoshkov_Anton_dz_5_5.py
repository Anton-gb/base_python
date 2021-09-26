src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

unique = set()
box = set()

for i in src:
    unique.add(i) if i not in box else unique.discard(i)
    box.add(i)

result = [num for num in src if num in unique]

print(result)
