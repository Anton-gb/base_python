import os
import shutil

with open('config.csv', 'r', encoding='utf-8') as f:
    for i in f:
        if i.count(' ') == 4:
            root_folder = i.strip()
            if not os.path.exists(root_folder):
                os.mkdir(root_folder)
        elif i.count(' ') == 8:
            folder_2 = i.strip()
            path_2 = os.path.join(root_folder, folder_2)
            if not os.path.exists(path_2):
                os.mkdir(path_2)
        elif i.count(' ') == 12:
            if i.strip().endswith('.py'):
                with open(os.path.join(path_2, i.strip()), 'w') as f_2:
                    pass
            else:
                folder_3 = i.strip()
                path_3 = os.path.join(path_2, folder_3)
                if not os.path.exists(path_3):
                    os.mkdir(path_3)
        elif i.count(' ') == 16:
            folder_4 = i.strip()
            path_4 = os.path.join(path_3, folder_4)
            if not os.path.exists(path_4):
                os.mkdir(path_4)
        elif i.count(' ') == 20:
            if i.strip().endswith('.html'):
                with open(os.path.join(path_4, i.strip()), 'w') as f_3:
                    pass

# shutil.rmtree(r'C:\IT\PyProject\Basics of the Python\base_python\my_project2')
