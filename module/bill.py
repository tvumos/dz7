"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

import module.dz_lib as lib
import os
import json

FILE_NAME = "bill.json"


ADD_BILL = "пополнение счета"
BUY = "покупка"
BUY_HISTORY = "история покупок"
EXIT = "выход"

bill_menu = (
    ADD_BILL,
    BUY,
    BUY_HISTORY,
    EXIT)


def main_menu(sum):
    """
    Меню
    1. пополнение счета'
    2. покупка
    3. история покупок
    4. выход
    :return:
    """
    print()
    print(lib.show_separator())
    print(f'Текущее состояние счета пользователя: {sum}')
    for number, item in enumerate(bill_menu, 1):
        print(f'{number}. {item}')
    print(lib.show_separator())


def load():
    """
    Загрузка состояния счета и истории покупок из бинарного файла
    """
    bill_template = {
        'sum': 0,
        'history': []
    }
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            result = json.load(f)
    else:
        result = bill_template
    return result


def save(bill_account):
    """
    Загрузка состояния счета и истории покупок из бинарного файла
    """
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(bill_account, f)


def my_bill_run():
    current_del = "\n"
    bill = dict(load())
    while True:
        main_menu(round(bill.get('sum', 0), 3))

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            user_sum = input('Укажите сумму пополнения счета, разделитель - точка: ')
            try:
                if float(user_sum) <= 0:      # float
                    raise Exception("Введено не корректное значение")
                bill["sum"] += round((float(user_sum)), 3)
            except:
                print("Указана не корректная сумма пополнения счета")
        elif choice == '2':
            pay_sum = input('Укажите сумму предполагаемой покупки, разделитель - точка: ')
            try:
                if float(pay_sum) <= 0:
                    raise Exception("Введено не корректное значение")
                pay_sum = round(float(pay_sum), 3)
            except:
                print("Указана не корректная сумма предполагаемой покупки")
                continue

            if bill.get('sum', 0) < pay_sum:
                print(f"Не хватает денег для покупки. На счете: {round(bill.get('sum', 0), 3)}")
            else:
                pay_name = input('Укажите название предполагаемой покупки: ')
                while not pay_name.isalpha():
                    pay_name = input('Укажите название предполагаемой покупки: ')
                bill.get('history', []).append(f"Товар: {pay_name}; Стоимость: {pay_sum}")
                bill['sum'] -= pay_sum
        elif choice == '3':
            if len(bill["history"]) == 0:
                print("Отсутствует история покупок")
            else:
                print("История покупок: ")
                print(current_del.join(bill["history"]))
        elif choice == '4':
            save(bill)
            break
        else:
            print('Неверный пункт меню')

    print('Приходите ещё!)')