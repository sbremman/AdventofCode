
import pandas as pd

def not_same_sign(a, b):
    return a * b < 0


def do_task_1(file_name):
    num_safe = 0
    #data = []
    with open(file_name, 'r') as file:
        for line in file:
            data = [int(x) for x in line.split()]

            prev_prev = data[0]
            prev = data[1]

            safe = 1

            for i in range(2, len(data)):

                prev_diff = data[i-1]-data[i-2]
                diff = data[i]-data[i-1]

                if (abs(prev_diff) > 3) or (abs(prev_diff) == 0) or (abs(diff) > 3) or (abs(diff) == 0) or not_same_sign(prev_diff, diff):
                    safe = 0
                    break

            num_safe += safe


    return num_safe

def do_task_2(file_name):

    num_safe = 0
    # data = []
    with open(file_name, 'r') as file:
        for line in file:
            data = [int(x) for x in line.split()]

            prev_prev = data[0]
            prev = data[1]

            safe = 1
            failed_index = 0

            for i in range(2, len(data)):

                prev_diff = data[i - 1] - data[i - 2]
                diff = data[i] - data[i - 1]

                if (abs(prev_diff) > 3) or (abs(prev_diff) == 0) or (abs(diff) > 3) or (
                        abs(diff) == 0) or not_same_sign(prev_diff, diff):
                    safe = 0
                    failed_index = i
                    break

            if safe == 0:
                for i in range(3):
                    copy_data = data.copy()
                    copy_data.pop(failed_index-i)
                    safe = 1
                    for j in range(2, len(copy_data)):

                        prev_diff = copy_data[j - 1] - copy_data[j - 2]
                        diff = copy_data[j] - copy_data[j - 1]

                        if (abs(prev_diff) > 3) or (abs(prev_diff) == 0) or (abs(diff) > 3) or (
                                abs(diff) == 0) or not_same_sign(prev_diff, diff):
                            safe = 0
                            break
                    if safe == 1:
                        break



            num_safe += safe

    return num_safe

