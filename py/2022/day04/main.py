#!/bin/python

with open("input.txt", "r") as file:
    sections = [x.split(",") for x in file.read().split("\n")]

sections.pop()

contained = 0

for elf1, elf2 in sections:
    elf1_range = [int(x) for x in elf1.split("-")]
    elf2_range = [int(x) for x in elf2.split("-")]

    if elf1_range[0] >= elf2_range[0] and elf1_range[1] <= elf2_range[1]:
        contained += 1
    elif elf2_range[0] >= elf1_range[0] and elf2_range[1] <= elf1_range[1]:
        contained += 1

print(contained)

# Part 2

overlap = 0

for elf1, elf2 in sections:
    elf1_range = [int(x) for x in elf1.split("-")]
    elf1_range[1] += 1
    elf2_range = [int(x) for x in elf2.split("-")]
    elf2_range[1] += 1

    intersection = len(set(range(*elf1_range)).intersection(set(range(*elf2_range))))
    if intersection:
        overlap += 1
    

print(overlap)
