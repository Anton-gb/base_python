def t_k():
    a = len(tutors) - len(klasses)
    for i, _ in enumerate(tutors):
        if i + a >= len(tutors):
            yield tutors[i], None
        else:
            yield tutors[i], klasses[i]


# Когда список klasses больше tutors
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

print(type(t_k()))

for gen in t_k():
    print(gen)

print('----------')
# Когда список klasses меньше tutors
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

for gen in t_k():
    print(gen)
