
import re
import numpy as np

def calculate_stuff(time, distance):

    best_distance = 0
    number_of_values = 0

    for i in range(time+1):
        speed = i
        running_time = time - i
        current_distance = running_time*speed
        if current_distance > distance:
            number_of_values += 1
        #print(current_distance)

    return number_of_values

def calculate_stuff_vector(time, distance):


    best_distance = 0
    number_of_values = 0
    time = time[0]

    #time = np.arange(0, time[0], 1)

    speeds = np.arange(0, time, 1)
    running_time = time - speeds
    current_distance = running_time * speeds
    """if current_distance > distance:
        number_of_values += 1"""
    # print(current_distance)

    test = np.count_nonzero(current_distance > distance)

    return number_of_values


def parse_data(data):

    data = data.split("\n")

    time = re.findall(r'\d+', data[0])
    time = [int(time_int) for time_int in time]
    distance = re.findall(r'\d+', data[1])
    distance = [int(distance_int) for distance_int in distance]

    return time, distance

def do_task_1(file_name):
    file = open(file_name, 'r')

    read = file.read()

    time, distance = parse_data(read)

    product = 1

    for i in range(len(time)):
        number_of_values = calculate_stuff(time[i], distance[i])
        product *= number_of_values


    return product


def do_task_2(file_name):
    file = open(file_name, 'r')

    read = file.read()

    time, distance = parse_data(read)

    product = 1

    test = calculate_stuff_vector(time, distance)

    return None