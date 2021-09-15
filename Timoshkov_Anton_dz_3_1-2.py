ru_eng = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def word_dict(word):
    if word in ru_eng:
        return ru_eng[word]
    else:
        box = [word[0].lower()]
        count = 1
        while count < len(word):
            box.append(word[count])
            count += 1
        w = ''.join(box)
        if w in ru_eng:
            return ru_eng.get(w).capitalize()


print(word_dict('nine'))
print(word_dict('Two'))
print(word_dict('TWo'))
