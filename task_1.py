def dishe_item_map(item):
    item_info = list(map(lambda info: info.strip(), item.split('|')))

    if len(item_info) < 3: return {}

    return {
        'ingredient_name': item_info[0],
        'quantity': int(item_info[1]),
        'measure': item_info[2]
    }


def parse_dishe(dishe_item_list):
    if len(dishe_item_list) < 3: return {}

    dishe_name = dishe_item_list[0]
    dishe_items = list(map(dishe_item_map, dishe_item_list[2:]))

    return dishe_name, dishe_items


def create_cook_book(file_path):
    cook_book = {}

    try:
        with open(file_path, 'r') as file:
            dishe = []

            for line in file:
                if line == '\n':
                    cook_name, cook_items = parse_dishe(dishe)
                    cook_book[cook_name] = cook_items

                    dishe = []
                else:
                    line_without_enter = line[:-1] if line[-1] == '\n' else line
                    dishe.append(line_without_enter)

            if len(dishe) > 0:
                cook_name, cook_items = parse_dishe(dishe)
                cook_book[cook_name] = cook_items

    except FileNotFoundError:
        print('No such file or directory:', file_path)

    return cook_book
