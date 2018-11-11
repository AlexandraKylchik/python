#Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

dir = [('dir_'+str(i+1)) for i in range(9)]

def dir_create(path):
    dir_path = os.path.join(os.getcwd(), path)
    try:
        os.mkdir(dir_path)
        print('Успешно перешел в папку ', dir_path)
    except:
        print('Невозмолжно перейти в папку ', dir_path)
for i in dir:
    dir_create(i)



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os

path = os.getcwd()
def show_dir(path):
    for _ in os.listdir(path):
        print(_)
show_dir(path)



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
from shutil import copy

destination_directory = os.path.abspath('destination_directory')
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

copy(__file__, destination_directory)



#функции для импорта в normal
def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - текущая директория')
        print('Успешно перешел в директорию ', dir_path)
    except:
        print(dir_path + ' - такой директории нет')




def delete_directory(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        os.rmdir(dir_path)
        print('Папка ',dir_path,' успешно удалена')
    except:
        print(dir_path + ' невозможно удалить')