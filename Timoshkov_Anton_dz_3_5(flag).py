import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(*args, n=1, flag=False):
    case = []
    count = 1
    while count <= n:
        box = []
        for i in args:
            box.append(f"{random.choice(i)}")
        case.append(box)

        if flag and case:
            for i in case:
                for j in i:
                    pass

        count += 1
    return case


print(get_jokes(nouns, adverbs, adjectives, n=4, flag=True))
