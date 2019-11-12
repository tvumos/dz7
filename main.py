"""
Домашнее задание № 6 - Трясцын Владимир
"""

import module.dz_lib as lib
from module.bill import my_bill_run
from module.victory import victory_run


CREATE_DIR = "Создать папку"
DELETE_FILE_DIR = "Удалить (файл/папку)"
COPY_FILE_DIR = "Копировать (файл/папку)"
SHOW_CURRENT_DIR = "Просмотр содержимого рабочей директории"
SHOW_FILES_IN_CURRENT_DIR = "Посмотреть только папки"
SHOW_DIRS_IN_CURRENT_DIR = "Посмотреть только файлы"
SHOW_SYSTEM_INFO = "Просмотр информации об операционной системе"
SHOW_AUTHOR = "Создатель программы"
GAME_VICTORY = "Играть в викторину"
GAME_BILL = "Мой банковский счет"
CHANGE_CURRENT_DIR = "Смена рабочей директории"
EXIT_PROGRAM = "Выход"


menu_actions = {
    EXIT_PROGRAM: lib.exit_program,
    CREATE_DIR: lib.create_dir,
    DELETE_FILE_DIR: lib.del_file_or_dir,
    COPY_FILE_DIR: lib.copy_file_or_dir,
    SHOW_CURRENT_DIR: lib.questions_save_listdir_in_file,
    SHOW_FILES_IN_CURRENT_DIR: lib.get_dir_in_current_dir,
    SHOW_DIRS_IN_CURRENT_DIR: lib.get_files_in_current_dir,
    SHOW_SYSTEM_INFO: lib.get_system_info,
    SHOW_AUTHOR: lib.show_author,
    GAME_VICTORY: victory_run,
    GAME_BILL: my_bill_run,
    CHANGE_CURRENT_DIR: lib.change_current_dir
}


def is_correct_input(choice):
    return choice.isdigit() and 0 <= int(choice) < len(menu_actions)


# Меню программы
while True:
    lib.print_menu(menu_actions)
    response = input('Укажите пункт меню -> ')
    if is_correct_input(response):
        menu_name = list(menu_actions.keys())[int(response)]
        action = menu_actions[menu_name]
        action()
    else:
        print("Не корректный вод пункта меню. Повторите ввод.")

