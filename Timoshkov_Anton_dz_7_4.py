import os

folder = 'some_data'

di = {
    250: 0,
    500: 0,
    750: 0,
    1000: 0
}

a = 100 * 2 ** 10

for root, dirs, files in os.walk(folder):
    for file in files:
        if os.stat(os.path.join(root, file)).st_size <= 250 * 2 ** 10:
            di[250] = di.get(250) + 1
        elif os.stat(os.path.join(root, file)).st_size <= 500 * 2 ** 10:
            di[500] = di.get(500) + 1
        elif os.stat(os.path.join(root, file)).st_size <= 750 * 2 ** 10:
            di[750] = di.get(750) + 1
        elif os.stat(os.path.join(root, file)).st_size <= 1000 * 2 ** 10:
            di[1000] = di.get(1000) + 1

print(di)
