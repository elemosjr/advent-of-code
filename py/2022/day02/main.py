#!/bin/python


def player_score1(opponent, player):
    switch_shape = {"X": 1, "Y": 2, "Z": 3}
    switch_outcome = {
        1: {"A": 3, "B": 0, "C": 6},
        2: {"A": 6, "B": 3, "C": 0},
        3: {"A": 0, "B": 6, "C": 3}
    }
    shape_score = switch_shape.get(player)
    outcome = switch_outcome.get(shape_score).get(opponent)
    return outcome + shape_score


# part 2

def player_score2(opponent, player):
    switch_outcome = {"X": 0, "Y": 3, "Z": 6}
    switch_shape = {
        0: {"A": 3, "B": 1, "C": 2},
        3: {"A": 1, "B": 2, "C": 3},
        6: {"A": 2, "B": 3, "C": 1}
    }
    outcome = switch_outcome.get(player)
    shape_score = switch_shape.get(outcome).get(opponent)
    return outcome + shape_score


if __name__ == "__main__":
  with open("input.txt", "r") as file:
      guide = [x.split(" ") for x in file.read().split("\n")]

  guide.pop()

  print(sum([player_score1(*x) for x in guide]))
  
  print(sum([player_score2(*x) for x in guide]))
