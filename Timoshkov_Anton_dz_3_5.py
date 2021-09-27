import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n=1):
    """
    Функция для вызова шуток
    :param n: кол-во шуток
    :return: функция возвращает список из шуток
    """
    box = []
    count = 1
    while count <= n:
        box.append(f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}")
        count += 1
    return box


print(get_jokes(2))
