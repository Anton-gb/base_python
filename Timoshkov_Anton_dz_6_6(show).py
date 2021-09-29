import sys

if len(sys.argv) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(f.read())
elif len(sys.argv) == 2:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for position, line in enumerate(f, 1):
            if position >= int(sys.argv[1]):
                print(line.replace('\n', ''))
elif len(sys.argv) == 3:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for position, line in enumerate(f, 1):
            if int(sys.argv[1]) <= position <= int(sys.argv[2]):
                print(line.replace('\n', ''))
            elif position > int(sys.argv[2]):
                break
else:
    print('Error')
