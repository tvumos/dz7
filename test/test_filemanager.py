import  os
import module.dz_lib as lib

def test_show_separator():
    assert lib.show_separator() == "=" * 55, f"dz_lib.show_separator(): {lib.show_separator()}"


def test_show_autor():
    assert lib.author() == f"Создатель программы: {lib.AUTHOR_PROGRAM}\nДата создания " \
                                  f"программы: {lib.DATE_CREATE}\n"


def test_create_dir_full_name():
    TEST_DIR = "test_dir"
    temp_dir = os.path.join(os.getcwd(), TEST_DIR)
    if os.path.exists(temp_dir):
        assert lib.create_dir_full_name(TEST_DIR) == False
    else:
        assert lib.create_dir_full_name(TEST_DIR) == True, f"Директория не существует. Ошибка при создании"


def test_del_file_or_dir_full_path():
    TEST_DIR = "test_dir"
    temp_dir = os.path.join(os.getcwd(), TEST_DIR)
    if os.path.exists(temp_dir):
        assert lib.del_file_or_dir_full_path(TEST_DIR) == True, f"Ошибка при удалении"
    else:
        assert lib.del_file_or_dir_full_path(TEST_DIR) == False, f"Файл/Директория не найдены"


