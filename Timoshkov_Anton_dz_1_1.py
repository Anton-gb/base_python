duration = int(input('Введите число для его конвертации: '))
second = duration

interval = [24*60*60, 60*60, 60]
time = []

for i in interval:
    d_h_m = second // i
    second -= d_h_m * i
    time.append(d_h_m)

if duration < 60:
    print(f'{second} сек')
elif 60 <= duration < 3600:
    print(f'{time[2]} мин {second} сек')
elif 3600 <= duration < 86400:
    print(f'{time[1]} час {time[2]} мин {second} сек')
else:
    print(f'{time[0]} дн {time[1]} час {time[2]} мин {second} сек')
