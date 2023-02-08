#!/bin/python

with open("input.txt", "r") as file:
    rucksacks = file.read().split("\n")

rucksacks.pop()


def char_value(duplicate):
    difference = 96
    if duplicate.isupper():
        difference = 38
    return ord(duplicate) - difference


def duplicate_priority(rucksack):
    half = int(len(rucksack)/2)
    left = rucksack[:half]
    right = rucksack[half:]
    for item in left:
        if item in right:
            duplicate = item
            break
    return char_value(duplicate)

print(sum([duplicate_priority(x) for x in rucksacks]))

# Part 2

groups = [rucksacks[(x*3):((x*3)+3)] for x in range(100)]
group = groups[0]


def group_value(group):
    duplicates = []
    for item in group[0]:
        if item in group[1]:
            duplicates.append(item)

    for duplicate in duplicates:
        if duplicate in group[2]:
            badge = duplicate

    return char_value(badge)

print(sum([group_value(x) for x in groups]))
