
import numpy as np

def do_task_1(file_name):

    lists = np.loadtxt(file_name)

    list_1 = lists[:, 0]
    list_1_sorted = np.sort(list_1)
    list_2 = lists[:, 1]
    list_2_sorted = np.sort(list_2)

    distances = np.abs(list_1_sorted - list_2_sorted)

    distances_sum = int(np.sum(distances))

    return distances_sum

def do_task_2(file_name):


    lists = np.loadtxt(file_name).astype(int)

    return_value = 0

    list_1 = lists[:, 0]
    list_2 = lists[:, 1]

    list_2_occurence_dict = {}

    for value in list_2:
        if value not in list_2_occurence_dict:
            list_2_occurence_dict[value] = 1
        else:
            list_2_occurence_dict[value] += 1

    for value in list_1:
        if value in list_2_occurence_dict:
            return_value += value * list_2_occurence_dict[value]

    return return_value

