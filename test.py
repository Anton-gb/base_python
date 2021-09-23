# numbers = [num_counts for num_counts in range(1, 11) for num in range(num_counts)]
# for i in numbers:
#     print(i)
# print(numbers)
#
# numbers = [
#     [num
#      for num in range(num_counts)]
#     for num_counts in range(1, 11)
# ]
# print(numbers)

mul_table = [
    a * b
    for a in range(1, 3)
    for b in range(4)
]
print(mul_table)
