src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res = [src[num + 1] for num in range(len(src) - 1) if src[num + 1] > src[num]]
print(res)

#
src = [30, 200, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 54, 53, 90]

res = [src[num + 1] for num in range(len(src) - 1) if src[num + 1] > src[num]]
print(res)
