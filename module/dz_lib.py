import os
import shutil
import platform
import sys


AUTHOR_PROGRAM = "Трясцын Владимир"
DATE_CREATE = "04.11.2019"


def show_separator():
    return "=" * 55

def author():
    return f"Создатель программы: {AUTHOR_PROGRAM}\nДата создания программы: {DATE_CREATE}\n"

def show_author():
    print(author())


def print_menu(menu_items):
    print(show_separator())
    print('            Консольный файловый менеджер')
    print(show_separator())
    # Выводим названи пункта меню и цифру начиная с 1
    for number, item in enumerate(menu_items, 0):
        print(f'{number} - {item}')
    print(show_separator())



def create_dir_full_name(full_dir):
    try:
        if os.path.exists(full_dir):
            print("ПРЕДУПРЕЖДЕНИЕ. Указанная директория уже существует. Укажите другое имя")
            return False
        else:
            os.mkdir(full_dir)
            print("Директория успешно создана\n")
            return True
    except:
        print("ПРЕДУПРЕЖДЕНИЕ. Указаны не допустимые символы в имени директории")
        return False



def create_dir():
    answer = input('\nУкажите имя создаваемой директории -> ')
    temp_dir = os.path.join(os.getcwd(), answer)
    create_dir_full_name(temp_dir)



def del_file_or_dir_full_path(full_path):
    try:
        if os.path.exists(full_path):       # Объект найден
            if os.path.isfile(full_path):   # Файл
                os.remove(full_path)
                print("Файл успешно удалён")
            elif os.path.isdir(full_path):  # Директория
                shutil.rmtree(full_path)
                print("Директория успешно удалена")
            return True
        else:
            print("ПРЕДУПРЕЖДЕНИЕ. Указанный файл/директория не найдена в текущей директории")
            return False
    except:
        print("ОШИБКА. Ошибка удаления файла/папки - отсутствует доступ к объекту")
        return False


def del_file_or_dir():
    answer = input('\nУкажите имя файла или папки для удаления -> ')
    temp_name = os.path.join(os.getcwd(), answer)
    del_file_or_dir_full_path(temp_name)


def copy_file_or_dir():
    print("")
    src_answer = input('Укажите имя исходного файла/папки для копирования -> ')
    dest_answer = input('Укажите новое имя файла/папки -> ')
    if src_answer == dest_answer:
        print("ПРЕДУПРЕЖДЕНИЕ. Исходное имя файла/папки совпадает с конечным именем. Повторите операцию.")
    else:
        src_answer = os.path.join(os.getcwd(), src_answer)
        dest_answer = os.path.join(os.getcwd(), dest_answer)
        if not os.path.exists(src_answer):
            print("ПРЕДУПРЕЖДЕНИЕ. Исходный файл/папка не найден")
        else:
            try:
                if os.path.isfile(src_answer):          # Файл
                    shutil.copy2(src_answer, dest_answer)
                    print("Файл успешно скопирован")
                elif os.path.isdir(src_answer):         # Директория
                    shutil.copytree(src_answer, dest_answer)
                    print("Каталог успешно скопирован")
            except IOError as e:
                print(f'ОШИБКА. Сообщение: {e.strerror}')


def questions_save_listdir_in_file():
    answer = input('Вы хотите сохранить содержимое рабочей директории в файл? (Да/Нет): ')
    while not answer.upper() in ["ДА", "НЕТ"]:
        answer = input('Повторите Ваш ответ. Вы хотите сохранить содержимое рабочей директории в файл? (Да/Нет): ')
    if answer.upper() == "ДА":
        find_in_current_dir(True)
    else:
        find_in_current_dir(False)


def find_in_current_dir(save_file):
    str_files = ""
    str_dirs = ""
    print("Список директорий и файлов в текущем каталоге:")
    for item in os.listdir("."):
        if (os.path.isfile(item)):
            if len(str_files) == 0:
                str_files += ("files: " + item)
            else:
                str_files += (", " + item)
        else:
            if len(str_dirs) == 0:
                str_dirs += ("dirs: " + item)
            else:
                str_dirs += (", " + item)
    # Вывод на экран
    print(str_files)
    print(str_dirs)
    # Сохранение в файл
    if (save_file == True):
        with open('listdir.txt', 'w', encoding='utf-8') as f:
            f.write(str_files + "\n")
            f.write(str_dirs + "\n")


def find_all_in_current_dir():
    folders = []
    print("Список директорий и файлов в текущем каталоге (с вложенными файлами/каталогами):")
    file_dir = os.listdir(".")
    for item in file_dir:
        folders.append(item)

    for address, dirs, files in folders:
        for dir in dirs:
            for file in files:
                print(f"Директория: {os.path.join(address, dir)}, Файл: {file}")


def get_files_in_current_dir():
    print("Список файлов в текущей директории:")
    print("\n".join(list(filter(lambda x: os.path.isfile(x), os.listdir(".")))))
    print()


def get_dir_in_current_dir():
    print("Список директорий в текущей директории:")
    print("\n".join(list(filter(lambda x: os.path.isdir(x), os.listdir(".")))))
    print()

def get_system_info():
    print()
    print("Информация о системе:")
    ops, name, oper_ver, build, proc, proc_fam = platform.uname()
    print(f"Операционная система: {ops}")
    print(f"Архитектура: {platform.architecture()}")
    print(f"Платформа: {sys.platform}")
    print(f"Версия операционной системы: {oper_ver}")
    print(f"Релиз операционной системы: {build}")
    print(f"Пользователь системы: {name}")
    print()
    print(f"Архитектура процессора: {proc}")
    print(f"Модель процессора: {proc_fam}")
    print()
    print(f"Версия Python: {' от '.join(platform.python_build())}")
    print(f"Версия компилятора Python: {platform.python_compiler()}")
    print(f"Реализация Python: {platform.python_implementation()}")
    print(f"Папка установки интерпретатора Python: {sys.prefix}")
    print()


def change_current_dir():
    dir = os.getcwd()
    print(f"Текущая рабочая директория: {dir}")
    answer = input('Укажите новую рабочую директорию: -> ')
    try:
        os.chdir(answer)
        print(f"Текущая рабочая директория: {os.getcwd()}")
    except BaseException as e:
        print(f'ОШИБКА. Сообщение: {e.strerror}')
        os.chdir(dir)
        print(f"Текущая рабочая директория не изменилась: {os.getcwd()}")



def exit_program():
    print('Программа завершается!')
    exit(0)





