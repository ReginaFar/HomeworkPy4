# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hours, rate, bonus = argv


def find_salary(hours_, rate_, bonus_):
    try:
        salary = (int(hours_) * float(rate_)) + float(bonus_)
    except ValueError:
        return
    return salary


print(f"{find_salary(hours, rate, bonus)}")
