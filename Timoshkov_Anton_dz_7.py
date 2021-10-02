import os
import shutil

folder = 'my_project'

name_folder = [
    'settings',
    'mainapp',
    'adminapp',
    'authapp'
]

if not os.path.exists(folder):
    os.mkdir(folder)

structure = [os.mkdir(os.path.join(folder, i)) for i in name_folder if not os.path.exists(os.path.join(folder, i))]

# shutil.rmtree(r'C:\IT\PyProject\Basics of the Python\base_python\my_project')
