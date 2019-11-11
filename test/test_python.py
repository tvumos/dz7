"""
Тесты для функций
filter, map, sorted
из библиотеки math: pi, sqrt, pow, hypot
"""


import math


def test_filter_del_2():
    a = list(filter(lambda x: x % 2 == 0, range(10)))
    assert len(a) == 5, f"len(a) = {len(a)} != 5"
    assert sum(a) == 20, f"sum(a) = {sum(a)} != 20"


def test_map_multi_3():
    b = list(map(lambda x: x * 3, range(6)))
    assert len(b) == 6, f"len(b) = {len(b)} != 6"
    assert sum(b) == 45, f"sum(b) = {sum(b)} != 45"



def genegate_list():
    """
    Возвращает список для последующей обработки
    :return: Список значений
    """
    #x = [10, 46, 23, 21, 49, 0, 1000, -12, -28]
    x = [10, 46, 23, 21, 49, 50, 42, 52, 0, 1000, -12, -28]
    #x = ["154", "Max", "Leo", "Dimon", "87", "-12", "0", "-28"]
    return x


def test_pi():
    """
    Проверка значения Пи
    Пи = 3,141592653589793238462643.....
    :return:
    """
    assert round(math.pi, 5) == 3.14159, f"Пи = {math.pi} != 3.14159"
    assert round(math.pi, 3) == 3.142, f"Пи = {math.pi} != 3.142"
    assert round(math.pi, 10) == 3.1415926536, f"Пи = {math.pi} != 3.1415926536"


def test_sqrt_list():
    ls_source = []
    map(lambda x: ls_source.append(x), range(20))
    ls_square = list(map(lambda x: x ** 2, ls_source))
    ls_result = list(map(lambda x: int(math.sqrt(x)), ls_square))
    assert ls_result == ls_source, f"Original list: {ls_source} \n Result list: {ls_result}"


def test_pow_list():
    ls_pow = list(map(lambda x: pow(x, x), range(10)))
    ls_test = list(map(lambda x: x ** x, range(10)))
    assert ls_pow == ls_test, f"ls_pow = {ls_pow} \n  ls_test = {ls_test}"


def test_hypot():
    assert round(math.hypot(2, 4), 3) == 4.472, f"math.hypot(2, 4) = {math.hypot(2, 4)}"
    assert round(math.hypot(-2, 1), 3) == 2.236, f"math.hypot(2, 4) = {math.hypot(-2, 1)}"
    assert round(math.hypot(3, 2), 3) == 3.606, f"math.hypot(2, 4) = {math.hypot(3, 2)}"
    assert round(math.hypot(4, -1), 3) == 4.123, f"math.hypot(2, 4) = {math.hypot(4, -1)}"
    assert round(math.hypot(5, 5), 5) == 7.07107, f"math.hypot(2, 4) = {math.hypot(5, 5)}"


def test_sorted_list():
    a = sorted(genegate_list(), reverse=True)   # Обратный порядок сортировки
    assert len(a) == len(genegate_list())
    assert a[0] == max(genegate_list())         # От максимального к минимальному
    b = sorted(genegate_list(), reverse=False)  # Стандартный порядок сортировки
    assert b[0] == min(genegate_list())         # От минимального к минимальному
