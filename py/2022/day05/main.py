#!/bin/python

import re


def init_stacks():
    with open("input.txt", "r") as file:
        lines = file.read().split("\n")
        crates = lines[:8]
        moves = lines[10:]
    crates.reverse()
    stacks = [[]]*9
    for line in crates:
        for stack in range(9):
            if not stack:
                string = line[0:3]
            else:
                string = line[(stack*3+stack):(stack*3+stack+3)]

            crate = re.findall("[A-Z]", string)
            if crate:
                stacks[stack] = stacks[stack] + crate
    return stacks


def move_crates(n, stack_from, stack_to):
    stack_from = int(stack_from) - 1
    stack_to = int(stack_to) - 1
    for i in range(int(n)):
        stacks[stack_to] = stacks[stack_to] + [stacks[stack_from].pop()]



def move_crates_9001(n, stack_from, stack_to):
    stack_from = int(stack_from) - 1
    stack_to = int(stack_to) - 1
    moving_crates = []
    for i in range(int(n)):
        moving_crates.append(stacks[stack_from].pop())
    moving_crates.reverse()
    stacks[stack_to] = stacks[stack_to] + moving_crates



stacks = init_stacks()

for move in moves:
    move_crates(*re.findall("[0-9]+", move))

print("".join([x[-1] for x in stacks]))

stacks = init_stacks()

for move in moves:
    move_crates_9001(*re.findall("[0-9]+", move))

print("".join([x[-1] for x in stacks]))