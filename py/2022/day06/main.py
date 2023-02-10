#!/bin/python
import numpy as np

with open("input.txt", "r") as file:
    datastream = file.read()

def is_marker(string):
    if len(np.unique(list(string))) != len(string):
        return False
    return True

def find_marker(datastream):
    for i in range(len(datastream)):
        if is_marker(datastream[i:(i+4)]):
            return i+4

print(find_marker(datastream))

# Part 2

def find_message(datastream):
    for i in range(len(datastream)):
        if is_marker(datastream[i:(i+14)]):
            return i+14

print(find_message(datastream))
