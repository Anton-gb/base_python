# duration = int(input('Введите число для его конвертации: '))
duration = 346140
second = duration

interval = [24 * 60 * 60, 60 * 60, 60]
time = []

for i in interval:
    d_h_m = second // i
    second -= d_h_m * i
    time.append(d_h_m)
time.append(second)

suffix = ['дн', 'час', 'мин', 'сек']

result = ''

for i in range(0, len(time)):
    if time[i] > 0:
        result += f'{time[i]} {suffix[i]} '
print(result)

# res = (f'{time[0]} дн {time[1]} час {time[2]} мин {second} сек' if duration >= 86400 else '') + (
#     f'{time[1]} час {time[2]} мин {second} сек' if 3600 <= duration < 86400 else '') + \
#       (f'{time[2]} мин {second} сек' if 60 <= duration < 3600 else '') + (f'{second} сек' if duration < 60 else '')
# print(res)

# if duration < 60:
#     print(f'{second} сек')
# elif 60 <= duration < 3600:
#     print(f'{time[2]} мин {second} сек')
# elif 3600 <= duration < 86400:
#     print(f'{time[1]} час {time[2]} мин {second} сек')
# else:
#     print(f'{time[0]} дн {time[1]} час {time[2]} мин {second} сек')
