def num_gen(n):
    for i in range(1, n+1, 2):
        yield i


for num in num_gen(11):
    print(num, end=', ')

print('')

n = 15
num_gen = (num for num in range(1, n+1, 2))
for num in num_gen:
    print(num, end=', ')
