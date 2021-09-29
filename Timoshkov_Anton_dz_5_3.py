def t_k():
    for i, _ in enumerate(tutors):
        if i < len(tutors):
            yield tutors[i], klasses[i]
        else:
            yield tutors[i], None
            

# Когда список klasses больше tutors
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

# print(type(t_k()))

result = ((tutor, klasses[i] if i < len(klasses) else None) for i, tutor in enumerate(tutors))

print(*result)

# for gen in t_k():
#     print(gen)

# print('----------')
# # Когда список klasses меньше tutors
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']
#
# for gen in t_k():
#     print(gen)
