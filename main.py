# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import itertools
import sys
import configparser
import timeit

import numpy as np
from itertools import permutations


def get_data(input_file):
    return np.loadtxt(input_file, dtype='i', skiprows=1), \
           np.loadtxt(input_file, dtype='i', max_rows=1, unpack=True)


def get_distance(path, data):
    dist = 0
    for i in range(1, len(path)):
        dist += data[path[i]][path[i - 1]]
    dist += data[path[0]][path[len(path) - 1]]
    return dist


def get_paths(num):
    paths1 = itertools.permutations(range(1, rows))
    final_paths = []
    print(type(paths1))
    for path in paths1:
        new_path = (0, *path, 0)
        final_paths.append(new_path)
    return tuple(final_paths)


def find_shortest_path(data, rows):
    shortest_path, shortest_dist = None, sys.maxsize
    paths = itertools.permutations(range(0, rows))
    for path in paths:
        dist = get_distance(path, data)
        if dist < shortest_dist:
            shortest_dist = dist
            shortest_path = path + (0,)
    return shortest_path, shortest_dist


def measure_time(data, rows, reps):
    times = []
    for i in range(0, reps):
        time = timeit.timeit("find_shortest_path(data, rows)", globals=globals(), number=1)
        times.append(time)
    return times

def get_file_names():
    config = configparser.ConfigParser()
    config.read("config.ini")
    input_file = config.get("files", "input_data")
    output_file = config.get("files", "output_data")
    return input_file, output_file


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file, output_file = get_file_names()
    data, rows = get_data(input_file)
    path, dist = find_shortest_path(data, rows)

    times = measure_time(data, rows, 1)
    with open(output_file, "a") as file:
        file.write(input_file)
        file.write(str(path) + "\t")
        file.write(str(dist) + "\n")
        file.write("\n".join((str(time)) for time in times))
        file.write("\n\n\n")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
