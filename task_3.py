import os


def join_files(file_path_list):
    dir = os.path.dirname(file_path_list[0])
    res_path = os.path.join(dir, 'result.txt')

    data = create_result_file_data(sort_data_list(file_path_list))

    with open(res_path, 'w') as document:
        document.write(data)


def file_data_map(file_path):
    file_data = ''
    line_length = 0
    file_name = os.path.basename(file_path)

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line_length += 1
                file_data += line

    except FileNotFoundError:
        print('No such file or directory:', file_path)

    return {"data": file_data, "line_count": line_length, "name": file_name}


def create_result_file_data(files_data_list):
    return '\n'.join(list(map(child_file_info_map, files_data_list)))


def sort_data_list(file_path_list):
    return sorted(get_file_data_list(file_path_list),
                  key=lambda file_data: file_data['line_count'])


def get_file_data_list(file_path_list):
    return list(map(file_data_map, file_path_list))


def child_file_info_map(info):
    return '\n'.join([info['name'], str(info['line_count']), info['data']])
