import pytest
import task_9_1
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_function_params

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_9_1, "generate_access_config")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_9_1.generate_access_config,
        param_count=2,
        param_names=["intf_vlan_mapping", "access_template"],
    )


def test_function_return_value():
    """
    Проверка работы функции
    """
    access_vlans_mapping = {
        "FastEthernet0/12": 10,
        "FastEthernet0/14": 11,
        "FastEthernet0/16": 17,
    }
    template_access_mode = [
        "switchport mode access",
        "switchport access vlan",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ]
    correct_return_value = [
        "interface FastEthernet0/12",
        "switchport mode access",
        "switchport access vlan 10",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
        "interface FastEthernet0/14",
        "switchport mode access",
        "switchport access vlan 11",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
        "interface FastEthernet0/16",
        "switchport mode access",
        "switchport access vlan 17",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ]

    return_value = task_9_1.generate_access_config(
        access_vlans_mapping, template_access_mode
    )
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Функция возвращает неправильное значение"


def test_function_return_value_different_args():
    """
    Проверка работы функции с другими аргументами
    """
    access_vlans_mapping = {
        "FastEthernet0/1": 101,
        "FastEthernet0/4": 121,
    }
    template_access_mode = [
        "switchport mode access",
        "switchport access vlan",
    ]
    correct_return_value = [
        "interface FastEthernet0/1",
        "switchport mode access",
        "switchport access vlan 101",
        "interface FastEthernet0/4",
        "switchport mode access",
        "switchport access vlan 121",
    ]

    return_value = task_9_1.generate_access_config(
        access_vlans_mapping, template_access_mode
    )
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Функция возвращает неправильное значение"
