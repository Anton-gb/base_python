import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(*args, n=1, flag=False):
    """
    Функция для генерации шуток
    :param args: в функцию передаются 3 списка слов
    :param n: кол-во шуток
    :param flag: аргумент разрешающий или запрещающий повтор шуток
    :return: возвращает список шуток
    """
    def test(li):
        i = random.randrange(len(li))
        case.append(li[i])
        li.pop(i)

    box = []
    first_list = args[0]
    second_list = args[1]
    third_list = args[2]
    count = 1
    while count <= n:
        case = []
        if flag:
            test(first_list)
            test(second_list)
            test(third_list)
            box.append(' '.join(case))
            if not first_list:
                if n > 5:
                    print('Ограничение по шуткам! не более 5 штук')
                break
            count += 1
        else:
            box.append(f"{random.choice(first_list)} {random.choice(second_list)} {random.choice(third_list)}")
            count += 1
    return box


print(get_jokes(nouns, adverbs, adjectives, n=7, flag=True))
