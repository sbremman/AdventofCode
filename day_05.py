
import numpy as np
import copy

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


def process_ranges(A, B):
    # Ensure the ranges are sorted (lower bound first)
    A.sort()
    B.sort()

    # Initialize the lists for intersection and differences
    intersection = []
    lower_diff = []
    upper_diff = []

    # Calculate intersection and differences
    if B[0] < A[0]:
        lower_diff = [B[0], min(A[0], B[1])]

    if B[1] > A[1]:
        upper_diff = [max(A[1], B[0]), B[1]]

    intersection_start = max(A[0], B[0])
    intersection_end = min(A[1], B[1])

    if intersection_start < intersection_end:
        intersection = [intersection_start, intersection_end]

    return intersection, lower_diff, upper_diff

def map_range_in_location_space_to_seed_range(map_lists):


    list_of_ranges = []
    list_of_adds = []

    for i in range(len(map_lists)):
        list_of_ranges.append([])
        list_of_adds.append([])
        current_list = map_lists[i]
        for j in range(len(current_list)):
            current_line = current_list[j]

            range_limits = [current_line[0], current_line[0]+current_line[2]]
            add = current_line[1]-current_line[0]
            list_of_ranges[i].append(range_limits)
            list_of_adds[i].append(add)


    temp_list_of_ranges = []
    for list in list_of_ranges:
        for entry in list:
            temp_list_of_ranges.append(entry)
    new_ranges = divide_ranges(temp_list_of_ranges)

    new_ranges = np.array(new_ranges)

    #new_ranges[:, 1] -= 1

    new_list_of_adds = [0 for _ in range(len(new_ranges))]

    for i in range(len(list_of_ranges)):
        prev_list_of_adds = copy.deepcopy(new_list_of_adds)
        test_2 = list_of_ranges[i]
        for k in range(len(list_of_ranges[i])):
            old_range = list_of_ranges[i][k]
            sum = 0
            j = 0
            while j < len(new_ranges):
                current_range = new_ranges[j]
                current_range_temp = current_range+prev_list_of_adds[j]
                """if old_range[0] <= current_range_temp[0]:
                    if current_range_temp[1] <= old_range[1]:"""

                # Check for the different types of overlap:
                # current_range_temp = [crt[0], crt[1]], old_range = [or[0], [or[1]]
                # or[0] <= crt[0] and crt[1] <= or[1] -> all good
                # or[0] > crt[0] and crt[1] <= or[1] -> create new lists [crt[0], or[0]] and [or[0], crt[1]]


                if check_overlap(old_range, current_range_temp):

                    intersection, lower_diff, upper_diff = process_ranges(old_range, current_range_temp)
                    not_complete_intersection = False
                    if len(lower_diff) != 0:
                        lower_diff = lower_diff-new_list_of_adds[j]
                        not_complete_intersection = True
                        new_ranges = np.append(new_ranges, np.array(lower_diff)[np.newaxis, :], axis=0)
                        new_list_of_adds.append(new_list_of_adds[j])
                        prev_list_of_adds.append(new_list_of_adds[j])

                    if len(upper_diff) != 0:
                        upper_diff = upper_diff-new_list_of_adds[j]
                        not_complete_intersection = True
                        new_ranges = np.append(new_ranges, np.array(upper_diff)[np.newaxis, :], axis=0)
                        new_list_of_adds.append(new_list_of_adds[j])
                        prev_list_of_adds.append(new_list_of_adds[j])

                    if not_complete_intersection:
                        intersection = intersection-new_list_of_adds[j]
                        new_ranges[j] = np.array(intersection)

                    #if old_range[1] != current_range[0]:
                    new_list_of_adds[j] += list_of_adds[i][k]
                    test = 1


                j += 1

            #print("test")

    # Sort arrays:
    arr1inds = new_ranges[:, 0].argsort()

    new_ranges = new_ranges[arr1inds]
    new_list_of_adds = np.array(new_list_of_adds)
    new_list_of_adds[arr1inds]

    return new_ranges, new_list_of_adds

def divide_ranges(ranges):
    # Flatten the list and sort the endpoints
    endpoints = sorted(set([point for range_ in ranges for point in range_]))

    # Create new ranges
    new_ranges = []
    for i in range(len(endpoints) - 1):
        # Skip if the range is not part of original ranges
        if any(start <= endpoints[i] < end for start, end in ranges):
            new_ranges.append([endpoints[i], endpoints[i+1]])

    return new_ranges

def check_overlap(A, B):
    return A[0] < B[1] and B[0] < A[1]


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

    seed_lists = map_lists[0]
    map_lists = map_lists[1:]

    map_lists.reverse()

    location_range_to_seed_range, location_to_seed_add = map_range_in_location_space_to_seed_range(map_lists)

    new_seed_list = []
    for i in range(0, len(seed_lists), 2):
        new_seed_list.append([seed_lists[i], seed_lists[i]+seed_lists[i+1]])


    for i in range(len(location_range_to_seed_range)):
        test = location_range_to_seed_range[i]
        test_1 = location_to_seed_add[i]
        location_to_seed_range = location_range_to_seed_range[i] + location_to_seed_add[i]
        for j in range(len(new_seed_list)):
            seed_range = new_seed_list[j]

            if check_overlap(location_to_seed_range, seed_range):
                print("test")



    lowest_location = 100000000000000

    """seeds = []

    for i in range(0, len(map_lists[0]), 2):
        for j in range(map_lists[0][i], map_lists[0][i]+map_lists[0][i+1]):
            seeds.append(j)

    for seed in seeds:
        location = get_location_of_seed(seed, map_lists[1:])

        lowest_location = min(lowest_location, location)"""

    return lowest_location

