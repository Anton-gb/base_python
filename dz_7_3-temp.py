# Не получилось скопировать шаблоны в папку templates
# Пробовал с помощью модуля shutil, не получилось...
# Пока эта тема дается с трудом


import os
import shutil


def create_templates(name_folder):
    name_f = 'templates'
    for root, dirs, files in os.walk(name_folder):
        if not os.path.exists(os.path.join(name_folder, name_f)):
            os.mkdir(os.path.join(name_folder, name_f))
        for _dir in dirs:
            # if _dir == 'templates':
            print(_dir)
            # shutil.copytree(os.path.join(os.getcwd(), _dir), os.path.join(root, name_f))


folder = 'my_project_3'

create_templates(folder)
