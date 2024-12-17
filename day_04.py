
import numpy as np


def do_task_1(file_name):

    return_value = 0

    data = []

    with open(file_name, 'r') as file:
        for line in file:
            new_data = list(line)

            if new_data[-1] == '\n':
                del new_data[-1]
            data.append(new_data)

    len_x_data = len(data)
    len_y_data = len(data[0])

    word_list = ['X', 'M', 'A', 'S']

    for i in range(len_x_data):
        for j in range(len_y_data):

            for x_dir in [-1, 0, 1]:
                for y_dir in [-1, 0, 1]:
                    word_found = 1
                    if x_dir == 0 and y_dir == 0:
                        break

                    else:
                        for word_idx in range(len(word_list)):
                            x_index = i+x_dir*word_idx
                            y_index = j+y_dir*word_idx
                            if (x_index < 0) or (x_index >= len_x_data) or (y_index < 0) or (y_index >= len_y_data):
                                word_found = 0
                                break
                            current_letter = data[x_index][y_index]
                            if current_letter != word_list[word_idx]:
                                word_found = 0
                                break
                            else:
                                pass
                        return_value += word_found

    return return_value


def do_task_2(file_name):
    import re

    return_value = 0

    return return_value
