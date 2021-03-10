import pytest
import task_17_4
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, read_all_csv_content_as_list

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_17_4, "write_last_log_to_csv")


def test_return_value(tmpdir):
    """
    Проверка работы функции
    """
    unique_data = [
        ["Name", "Email", "Last Changed"],
        ["Kuiil", "i_have_spoken@gmail.com", "20/04/2015 21:56"],
        ["Chewie", "chewbacca@gmail.com", "10/02/2019 22:45"],
        ["Cara Dune", "shocktrooper@gmail.com", "11/10/2019 14:05"],
        ["Mandalorian", "mandalorian176@gmail.com", "10/11/2019 12:11"],
        ["D-O", "do@gmail.com", "15/12/2019 22:45"],
        ["BB-8", "bb8@gmail.com", "16/12/2019 17:20"],
        ["C-3PO", "c3po@gmail.com", "16/12/2019 17:24"],
        ["Ben Solo", "supreme_leader@gmail.com", "21/12/2019 12:25"],
        ["R2D2", "r2d2@gmail.com", "23/10/2018 05:10"],
    ]
    source_filename = "mail_log.csv"
    dest_filename = tmpdir.mkdir("test_tasks").join("output.csv")
    return_value = task_17_4.write_last_log_to_csv(source_filename, dest_filename)
    csv_content = read_all_csv_content_as_list(dest_filename)
    correct_return_value = sorted(unique_data)

    assert (
        return_value == None
    ), f"По заданию функция должна возвращать None, а возвращает {type(return_value).__name__}"
    assert (
        sorted(csv_content) == correct_return_value
    ), "Функция возвращает неправильное значение"
