
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

    symbol_adjacency_matrix = np.full(symb_adj_shape, True)

    for i in range(array_of_symbols.shape[0]):
        for j in range(array_of_symbols.shape[1]):

            if array_of_symbols[i][j] == '.':
                pass

            elif array_of_symbols[i][j].isnumeric():
                pass

            else:
                directions_to_search = [-1, 0, 1]
                for up_down in directions_to_search:
                    vert_search = i + up_down

                    for left_right in directions_to_search:
                        hori_search = j + left_right

                        if array_of_symbols[vert_search][hori_search].isnumeric():
                            symbol_adjacency_matrix[vert_search][hori_search] = False



    test = array_of_symbols[symbol_adjacency_matrix]

    print("test")



def do_task_1(file_name):
    file = open(file_name, 'r')

    Lines = file.readlines()

    listed_list = parse_input_to_listed_lists(Lines)

    array_of_symbols = np.array(listed_list)

    padded_array_of_symbols = np.pad(array_of_symbols, 1, 'constant', constant_values='.')

    test = make_array_of_symbol_adjacency(padded_array_of_symbols)

    print("test")


