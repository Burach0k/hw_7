import task_1
import os
from functools import reduce


def get_shop_list_by_dishes(dishes, person_count):
    path = os.path.join('./', 'files_for_task_1', 'test.txt')
    cook_book = task_1.create_cook_book(path)

    return reduce(
        lambda prev_dishe, dishe: dish_count_info_reducer(
            prev_dishe, cook_book[dishe], person_count), dishes, {})


def dish_count_info_reducer(prev_dishe, dishe_info_list, person_count):
    item = reduce(
        lambda prev_element, dishe_info: dish_ifno_reduce(
            prev_element, dishe_info, person_count), dishe_info_list, {})

    for attr, value in item.items():
        if attr in prev_dishe:
            prev_dishe[attr].quantity += value.quantity
        else:
            prev_dishe[attr] = value

    return prev_dishe


def dish_ifno_reduce(prev_element, dishe_info, person_count):
    ingredient_name = dishe_info['ingredient_name']

    prev_element[ingredient_name] = {
        'measure': dishe_info['measure'],
        'quantity': dishe_info['quantity'] * person_count
    }

    return prev_element
