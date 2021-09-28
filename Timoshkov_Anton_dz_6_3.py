with open('users.csv', 'r', encoding='utf-8') as f:
    users_file = f.read()

with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby_file = f.read()

users = users_file.replace(',', ' ').strip().split('\n')
hobby = hobby_file.replace(',', ', ').strip().split('\n')

users_dict = {}

if len(users) >= len(hobby):
    for i, user in enumerate(users):
        if i < len(hobby):
            users_dict[user] = hobby[i]
        else:
            users_dict[user] = None
    print(users_dict)
else:
    print('Код ошибки: 1')
