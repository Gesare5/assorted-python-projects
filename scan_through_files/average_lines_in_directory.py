#!/usr/bin/env python3

import os

path_to_directory = "./sample_directory"


def get_path_list(main_path):
    path_list = []
    for root, dirs, files in os.walk(main_path, topdown=True):
        for name in files:
            path_list.append(os.path.join(root, name))
    return path_list


def count_lines(path_list):
    total_number_of_lines = 0
    for path in path_list:
        # The 'b' in the mode specifier in the open() states that the file shall be treated as binary,
        # so contents will remain a bytes. No decoding attempt will happen this way.
        # Avoids Error: utf-8' codec can't decode byte 0x89 in position 0: invalid start byte
        with open(path, "rb") as new_file:
            total_number_of_lines += len(new_file.readlines())
    return total_number_of_lines


def calculate_average_lines_per_file(total_lines, path_list):
    average_lines = total_lines / len(path_list)
    return average_lines


path_list = get_path_list(path_to_directory)
total_lines = count_lines(path_list)
average_lines = calculate_average_lines_per_file(total_lines, path_list)
print(round(average_lines))
