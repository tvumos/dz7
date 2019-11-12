import os
import module.dz_lib as lib
import module.bill as bill

def test_find_in_current_dir_true():
    if os.path.exists('listdir.txt'):
        os.remove('listdir.txt')
    lib.find_in_current_dir(True)   # Сохраняем файл в текущей директории
    assert os.path.exists('listdir.txt') == True, "Отсутствует файл listdir.txt"


def test_find_in_current_dir_false():
    if os.path.exists('listdir.txt'):
        os.remove('listdir.txt')
    lib.find_in_current_dir(False)   # Не сохраняем содержимое текущей директории файл
    assert os.path.exists('listdir.txt') == False, "Создан файл в listdir.txt"


def test_load():
    account = bill.load()
    assert account is not None, "Объект не определён"
    assert 'sum' in account, "Отсутствует ключ для сохранённого значения суммы счета"
    assert 'history' in account, "Отсутствует ключ для сохранённого списка покупок"
    assert account['sum'] >= 0, "Не корректное значение суммы счета. Отрицательное значение"


def test_save():
    bill_template = {
        'sum': 1000.90,
        'history': ["Покупка 1, стоимость 10", "Покупка 2, стоимость 20"]
    }
    bill.save(bill_template)
    new_bill = bill.load()
    assert bill_template == new_bill, "Ошибка сохранения объекта и загрузки. Объект изменён"
    if os.path.exists('bill.json'):
        os.remove('bill.json')






