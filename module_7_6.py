import time
import os
print('\033[30m\033[47mДомашнее задание по теме "Файлы в операционной системе".\033[0m')
print('\033[30m\033[47mЗадача Создайтm новый проект или продолжитm работу в текущем проекте.\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()
if os.path.exists('directory'):
    os.chdir('directory')
else:
    os.mkdir('directory')
    os.chdir('directory')

way = [f for f in os.listdir() if os.path.isfile(f)]
if way == ['main.py']:
    pass
else:
    f = open('main.py', 'w+')
    f.write("print('Hello Urban!')")
    f.close()
files = [f for f in os.listdir() if os.path.isfile(f)]
directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.abspath(os.path.join(file, os.pardir))
        filetime = os.stat(file).st_mtime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(file).st_size
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file};\nПуть: {filepath};\nРазмер: {filesize} байт;\nВремя изменения: {formatted_time}'
              f';\nРодительская директория: {parent_dir}.')
print()
print(thanks)
