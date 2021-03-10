import pytest


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_task_stdout(capsys):
    """
    Проверка работы задания
    """
    import task_4_1

    out, err = capsys.readouterr()
    correct_stdout = (
        "ip nat inside source list ACL interface GigabitEthernet0/1 overload"
    )
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        out.strip() == correct_stdout
    ), "На стандартный поток вывода выводится неправильная строка"
