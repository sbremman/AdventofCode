
import numpy as np

def split_into_eight_lists(input_string):


    string_lists = input_string.split('\n\n')

    int_lists = []

    for str_list in string_lists:
        int_lists.append([])
        i = 0
        while i + 1 < len(str_list):
            i += 1
            symbol = str_list[i]
            if symbol.isnumeric():
                int_lists[-1].append([])
                while symbol.isnumeric():
                    int_lists[-1][-1].append(symbol)
                    i += 1

                    if i+1 > len(str_list):
                        break
                    else:
                        symbol = str_list[i]

    new_int_lists = []
    for list in int_lists:
        new_int_lists.append([])
        for list_n in list:
            new_int_lists[-1].append(int(''.join(list_n)))


    for i in range(1, len(new_int_lists)):
        new_int_lists[i] = np.array(new_int_lists[i]).reshape(int(len(new_int_lists[i])/3), 3)

    return new_int_lists

def get_location_of_seed(seed, map_lists):

    source = seed

    for array in map_lists:
        source_larger = np.where(array[:, 1] <= source, True, False)
        source_smaller = np.where(array[:, 1]+array[:, 2] > source, True, False)

        test = source_smaller*source_larger

        if np.all(test == False):
            destination = source

        else:
            test_array = array[test]

            destination = test_array[:, 0] + source - test_array[:, 1]

        source = destination

    return source[0]




def do_task_1(file_name):
    file = open(file_name, 'r')

    read = file.read()

    map_lists = split_into_eight_lists(read)

    lowest_location = 100000000000000

    for seed in map_lists[0]:
        location = get_location_of_seed(seed, map_lists[1:])

        lowest_location = min(lowest_location, location)

    return lowest_location


def do_task_2(file_name):
    file = open(file_name, 'r')

    read = file.read()

    map_lists = split_into_eight_lists(read)

    lowest_location = 100000000000000

    seeds = []

    for i in range(0, len(map_lists[0]), 2):
        for j in range(map_lists[0][i], map_lists[0][i]+map_lists[0][i+1]):
            seeds.append(j)

    for seed in seeds:
        location = get_location_of_seed(seed, map_lists[1:])

        lowest_location = min(lowest_location, location)

    return lowest_location