def thesaurus(*name_list):
    name_dict = {}
    for name in name_list:
        name_dict.setdefault(name[0], list(filter(lambda x: x.startswith(name[0]), name_list)))
    return name_dict


def test(res_dict):
    for key in sorted(res_dict):
        val = res_dict[key]
        print(f"'{key}': {val}")


result = thesaurus("Иван", "Мария", "Петр", "Илья", "Аня", "Аня")
print(result)

# сортировка словаря
print('---------')
test(result)
