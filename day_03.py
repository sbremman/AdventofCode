
import numpy as np

def parse_input_to_listed_lists(input_list_of_strings):

    listed_list = []
    for line in input_list_of_strings:
        listed_string = list(line)
        if listed_string[-1] == '\n':
            del(listed_string[-1])

        listed_string = np.array(listed_string)
        listed_list.append(listed_string)

    return listed_list

def make_array_of_symbol_adjacency(array_of_symbols):

    symb_adj_shape = list(array_of_symbols.shape)

    symbol_adjacency_matrix = np.full(symb_adj_shape, False)
    non_numeric_at_pos_matrix = np.full(symb_adj_shape, False)

    for i in range(array_of_symbols.shape[0]):
        for j in range(array_of_symbols.shape[1]):
            if array_of_symbols[i][j] == '.':
                non_numeric_at_pos_matrix[i][j] = True

            elif array_of_symbols[i][j].isnumeric():
                pass

            else:
                non_numeric_at_pos_matrix[i][j] = True
                directions_to_search = [-1, 0, 1]
                for up_down in directions_to_search:
                    vert_search = i + up_down

                    for left_right in directions_to_search:
                        hori_search = j + left_right

                        if array_of_symbols[vert_search][hori_search].isnumeric():
                            symbol_adjacency_matrix[vert_search][hori_search] = True

    for i in range(array_of_symbols.shape[0]):
        for j in range(array_of_symbols.shape[1]):

            if array_of_symbols[i][j].isnumeric():
                # Search left:
                curr_j = j
                while symbol_adjacency_matrix[i][curr_j]:
                    curr_j -= 1
                    if array_of_symbols[i][curr_j].isnumeric():
                        symbol_adjacency_matrix[i][curr_j] = True

                # Search right:
                curr_j = j
                while symbol_adjacency_matrix[i][curr_j]:
                    curr_j += 1
                    if array_of_symbols[i][curr_j].isnumeric():
                        symbol_adjacency_matrix[i][curr_j] = True




    combined_matrix = symbol_adjacency_matrix + non_numeric_at_pos_matrix

    test = array_of_symbols[combined_matrix]

    total_number_list = []

    i = 0
    while i < len(test):
        move_right = 0
        number_list = []
        while test[i].isnumeric():
            number_list.append(test[i])
            i += 1

        if len(number_list) != 0:
            number = ''.join(number_list)
            total_number_list.append(int(number))

        else:
            i += 1



    test = sum(total_number_list)

    return test


def make_array_of_symbol_adjacency_2(array_of_symbols):

    symb_adj_shape = list(array_of_symbols.shape)

    symbol_adjacency_matrix = np.full(symb_adj_shape, False)
    non_numeric_at_pos_matrix = np.full(symb_adj_shape, False)

    for i in range(array_of_symbols.shape[0]):
        for j in range(array_of_symbols.shape[1]):
            if array_of_symbols[i][j] == '.':
                non_numeric_at_pos_matrix[i][j] = True

            elif array_of_symbols[i][j].isnumeric():
                pass

            elif array_of_symbols[i][j] == '*':
                part_numbers = 0
                non_numeric_at_pos_matrix[i][j] = True
                directions_to_search = [-1, 0, 1]
                for up_down in directions_to_search:
                    vert_search = i + up_down
                    for left_right in directions_to_search:
                        hori_search = j + left_right

                        if array_of_symbols[vert_search][hori_search].isnumeric():
                            if symbol_adjacency_matrix[vert_search][hori_search+1] == False:
                                if symbol_adjacency_matrix[vert_search][hori_search - 1] == False:
                                    part_numbers += 1
                            symbol_adjacency_matrix[vert_search][hori_search] = True

                if part_numbers != 2:
                    for up_down in directions_to_search:
                        vert_search = i + up_down
                        for left_right in directions_to_search:
                            hori_search = j + left_right
                            if array_of_symbols[vert_search][hori_search].isnumeric():
                                symbol_adjacency_matrix[vert_search][hori_search] = False


            else:
                non_numeric_at_pos_matrix[i][j] = True

    for i in range(array_of_symbols.shape[0]):
        for j in range(array_of_symbols.shape[1]):

            if array_of_symbols[i][j].isnumeric():
                # Search left:
                curr_j = j
                while symbol_adjacency_matrix[i][curr_j]:
                    curr_j -= 1
                    if array_of_symbols[i][curr_j].isnumeric():
                        symbol_adjacency_matrix[i][curr_j] = True

                # Search right:
                curr_j = j
                while symbol_adjacency_matrix[i][curr_j]:
                    curr_j += 1
                    if array_of_symbols[i][curr_j].isnumeric():
                        symbol_adjacency_matrix[i][curr_j] = True




    combined_matrix = symbol_adjacency_matrix + non_numeric_at_pos_matrix

    test = array_of_symbols[combined_matrix]

    total_number_list = []

    i = 0
    while i < len(test):
        move_right = 0
        number_list = []
        while test[i].isnumeric():
            number_list.append(test[i])
            i += 1

        if len(number_list) != 0:
            number = ''.join(number_list)
            total_number_list.append(int(number))

        else:
            i += 1



    test = sum(total_number_list)

    return test



def do_task_1(file_name):
    file = open(file_name, 'r')

    Lines = file.readlines()

    listed_list = parse_input_to_listed_lists(Lines)

    array_of_symbols = np.array(listed_list)

    padded_array_of_symbols = np.pad(array_of_symbols, 1, 'constant', constant_values='.')

    test = make_array_of_symbol_adjacency(padded_array_of_symbols)

    return test


def do_task_2(file_name):
    file = open(file_name, 'r')

    Lines = file.readlines()

    listed_list = parse_input_to_listed_lists(Lines)

    array_of_symbols = np.array(listed_list)

    padded_array_of_symbols = np.pad(array_of_symbols, 1, 'constant', constant_values='.')

    test = make_array_of_symbol_adjacency_2(padded_array_of_symbols)

    return test


