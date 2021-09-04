numbers = []

for i in range(1, 1001):
    if i % 2 != 0:
        numbers.append(i ** 3)

print(numbers)

sum_num = 0

for i in numbers:
    case = i
    last_num = i % 10
    while i >= 10:
        if i > 100:
            i = i // 10
            num = i % 10
            last_num += num
        else:
            i = i // 10
            last_num += i
    if last_num % 7 == 0:
        sum_num += case

print(sum_num)

a = 0
for i in numbers:
    i += 17
    numbers[a] = i
    a += 1

print(numbers)

sum_num = 0

for i in numbers:
    case = i
    last_num = i % 10
    while i >= 10:
        if i > 100:
            i = i // 10
            num = i % 10
            last_num += num
        else:
            i = i // 10
            last_num += i
    if last_num % 7 == 0:
        sum_num += case

print(sum_num)
