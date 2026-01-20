"""
Author: Dietrich Geisler
Creation Date: 4/22/2025

A collection of utilities for the "getting to know you" analysis functions
"""

# Get the CSV module to read our data
import csv

def read_data(data_path): 
    """
    Read the data from the file at data_path
    and return it as a list of lists
    """

    # Open the data file
    data = []
    with open(data_path, mode='r', encoding='utf-8', errors='ignore') as data_file:
        first = True # skip the first line
        for row in csv.reader(data_file, delimiter=','):
            if first:
                first = False
            else:
                data.append(row)

    # Cast the data to a list before returning
    return list(data)

def print_lines(result):
    """
    Prints each line of result one at a time
    """
    for line in result:
        print(line)

def print_nested_lines(result):
    """
    Prints each list inside of result line-by-line
    Adds a newline between each
    """
    for lst in result:
        # Give a nice error message if we don't have a list result 
        message = f'Each element of result must be a list, {lst} is not'
        assert isinstance(lst, list), message
        print_lines(lst)
        print() # add the extra newline

def print_dictionary_pretty(result):
    """
    Prints a dictionary with lines between each key/value pair
    """
    print('{')
    for key in result:
        print(f'\t{key} : {result[key]},')
    print('}')