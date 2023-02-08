#!/bin/python

FILENAME = "input.txt"


def elf_total(data):
  calories = map(lambda x: int(x), data)
  total = sum(calories)
  return total

with open(FILENAME) as file:
  data = list(map(lambda x: x.split("\n"),
              file.read().split("\n\n")))

elves = list(map(lambda x: elf_total(x), data[:-1]))
elves.sort()

most_cal = elves[-1]
three_most_cal = sum(elves[-3:])

print(most_cal)
print(three_most_cal)
