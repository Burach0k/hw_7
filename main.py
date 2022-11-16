import task_1
import task_2
import task_3
import os

path = os.path.join('./', 'files_for_task_1', 'test.txt')
print(task_1.create_cook_book(path))

print('\n-------------------------\n')

print(task_2.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

print('\n-------------------------\n')

path_1 = os.path.join('./', 'files_for_task_3', '1.txt')
path_2 = os.path.join('./', 'files_for_task_3', '2.txt')
path_3 = os.path.join('./', 'files_for_task_3', '3.txt')
task_3.join_files([path_1, path_2, path_3])