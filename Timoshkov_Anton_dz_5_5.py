src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

uniq = set()
_ts = set()

for i in src:
    uniq.add(i) if i not in _ts else uniq.discard(i)
    _ts.add(i)

result = [num for num in src if num in uniq]

print(result)
