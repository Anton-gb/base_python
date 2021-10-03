import os
import json


def count_dash(line):
    count = 0
    for i in line:
        if i == '-':
            count += 1
        else:
            break
    return count


def find_end(conf, level):
    for i in conf:
        if count_dash(i) < level:
            return conf.index(i)
    return len(conf) + 1


def parsing(config_list):
    config_dict = {}
    indx = 0
    len_list = len(config_list)
    while indx < len_list:
        word = config_list[indx]
        key = config_list[indx].replace('-', '')
        a = count_dash(word)
        b = 0
        if indx + 1 < len_list:
            b = count_dash(config_list[indx + 1])
        if a < b:
            # Тогда есть вложенность
            start = indx + 1
            end = find_end(config_list[start:], b)
            config_dict[key] = parsing(config_list[start:start + end])
            indx = start + end
        else:
            config_dict[key] = None
            indx += 1
    return config_dict


def create_dir(res_dict, dir_path=os.getcwd()):
    for key, val in res_dict.items():
        if '.' in key:
            with open(os.path.join(dir_path, key), 'w') as fb:
                pass
        else:
            os.mkdir(os.path.join(dir_path, key))
            create_dir(val, os.path.join(dir_path, key))


def create_templates():
    pass


file_name = 'config.yaml'

with open(file_name, 'r') as f:
    config = [line.replace('\n', '').replace('    ', '-') for line in f]

res = parsing(config)

print(json.dumps(res, indent=2))

create_dir(res)

create_templates()
