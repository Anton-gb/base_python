def thesaurus(*name_list):
    lastname_dict = {}
    for name in name_list:
        index = name.find(' ')
        lastname_dict.setdefault(name[index + 1], dict())
        for key, val in lastname_dict.items():
            if name[index + 1] == key:
                val.setdefault(name[0], list())
        for key_2, val_2 in lastname_dict.items():
            for key_3, val_3 in val_2.items():
                if name[0] == key_3 and name[index + 1] == key_2:
                    val_3.append(name)
    return lastname_dict


def test(f):
    for key in sorted(f):
        val = f[key]
        print(f"'{key}': {val}")


result = thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(result)

# сортировка словаря
print('---------')
test(result)
