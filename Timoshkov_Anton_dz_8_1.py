import re


def email_parse(email):
    parse_dict = {}
    domen = re.compile(r"@\w+.\w+")
    name = re.compile(r"([^@]+)(?=[@*])")
    try:
        parse_dict['username'] = name.findall(email)[0]
        parse_dict['domain'] = domen.findall(email)[0]
        print(parse_dict)
    except IndexError as e:
        raise ValueError(f"{email} is wrong")


email_parse('someone@geekbrains.ru')
