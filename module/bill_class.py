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
import pickle
import os


class Bill(object):
    """
    Класс сохраняющий состояние текущего счета пользователя и историю покупок
    """

    FILE_NAME = "bill.bin"

    def __init__(self, sum = 0, histoty = []):
        """Constructor"""
        self.histoty = histoty
        self.sum = sum

    def get_account(self):
        return self.sum

    def get_history(self):
        return self.histoty

    def add_bill(self, add_sum):
        self.sum += add_sum

    def add_buy(self, purchase):
        for key, value in purchase.items():
            self.sum -= value
            self.histoty.append(f"товар: {key}, стоимость: {value}")

    def load(self):
        """
        Загрузка состояния счета и истории покупок из бинарного файла
        """
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'rb') as f:
                self = Bill(pickle.load(f))

    def save(self):
        """
        Сохранение состояния счета и истории покупок в бинарный файл
        """
        with open(self.FILE_NAME, 'wb') as f:
            pickle.dump(self, f)


# if __name__ == "__main__":
#     bill = Bill()
#     bill.load()
#     bill.add_bill(50)
#     bill.add_buy({"машина": 4.6})
#     bill.add_buy({"гараж": 5.6})
#     print(bill.get_account())
#     print(bill.get_history())
#     bill.save()
#     print("=" * 50)
#     bill.add_buy({"test save": 2.6})
#     bill.save()
#     #bill.add_buy({"Товар 3": 6.6})
#     print("="*50)
#     bill.load()
#     print(bill.get_account())
#     print(bill.get_history())
#     #bill.save_json()



ADD_BILL = "пополнение счета"
BUY = "покупка"
BUY_HISTORY = "история покупок"
EXIT = "выход"
bill_menu = (
    ADD_BILL,
    BUY,
    BUY_HISTORY,
    EXIT)

def main_menu():
    """
    Меню
    1. пополнение счета'
    2. покупка
    3. история покупок
    4. выход
    :return:
    """
    lib.show_separator()
    for number, item in enumerate(bill_menu, 1):
        print(f'{number}. {item}')
    lib.show_separator()




def my_bill_run():
    current_del = "\n"
    bill = Bill()
    bill.load()
    #account = float("0.0")
    #pay_history = []
    while True:
        main_menu()

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            user_sum = input('Укажите сумму пополнения счета, разделитель - точка: ')
            try:
                if float(user_sum) <= 0:      # float
                    raise Exception("Введено не корректное значение")
                bill.add_bill(float(user_sum))
                #account += float(user_sum)
            except:
                print("Указана не корректная сумма пополнения счета")
            print(f"Текущее состояние счета: {bill.sum}")
        elif choice == '2':
            pay_sum = input('Укажите сумму предполагаемой покупки, разделитель - точка: ')
            try:
                if float(pay_sum) <= 0:
                    raise Exception("Введено не корректное значение")
                pay_sum = float(pay_sum)
            except:
                print("Указана не корректная сумма предполагаемой покупки")
                continue
            if bill.sum < pay_sum:
                print(f"Не хватает денег для покупки. На счете: {bill.sum}")
            else:
                pay_name = input('Укажите название предполагаемой покупки: ')
                #account -= pay_sum
                while not pay_name.isalpha():
                    pay_name = input('Укажите название предполагаемой покупки: ')
                #pay_history.append(f"Товар: {pay_name}; Стоимость: {pay_sum}")
                bill.add_buy({pay_name: pay_sum})
                print(f"Текущее состояние счета: {bill.sum}")
        elif choice == '3':
            if len(bill.histoty) == 0:
                print("Отсутствует история покупок")
            else:
                print("История покупок: ")
                print(current_del.join(bill.histoty))
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

    print('Приходите ещё!)')