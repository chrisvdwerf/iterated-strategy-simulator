from __future__ import annotations
from strategy import *
from typing import Dict, List


class GameResult:
    scores: Dict[Strategy, int]

    def __init__(self):
        self.scores = {}

    def get_score(self, strategy: Strategy):
        return self.scores[strategy]

    def add_to_score(self, strategy: Strategy, value: int):
        if strategy not in self.scores:
            self.scores[strategy] = 0

        self.scores[strategy] += value

    def combine(self, result: GameResult):
        for strategy, score in result.scores.items():
            self.add_to_score(strategy, score)

    def __str__(self):
        print("=== Score begin ===")
        for strategy, score in self.scores.items():
            print(f"{strategy} - {score}")
        print("=== Score end ===")
        return ""


class Simulator():
    def play_single_game(self, stratA: Strategy, stratB: Strategy, rounds: int) -> GameResult:
        result = GameResult()
        movesA: List[int] = list()
        movesB: List[int] = list()

        for i in range(rounds):
            moveA = stratA.get_next_move(movesB)
            moveB = stratB.get_next_move(movesA)

            if moveA == 0 and moveB == 0:
                result.add_to_score(stratA, 1)
                result.add_to_score(stratB, 1)

            elif moveA == 1 and moveB == 0:
                result.add_to_score(stratA, 0)
                result.add_to_score(stratB, 5)

            elif moveA == 0 and moveB == 1:
                result.add_to_score(stratA, 5)
                result.add_to_score(stratB, 0)

            elif moveA == 1 and moveB == 1:
                result.add_to_score(stratA, 3)
                result.add_to_score(stratB, 3)

            else:
                raise ValueError(f"invalid combination {moveA}, {moveB}")

            movesA.append(moveA)
            movesB.append(moveB)

        return result

    def play_round_of_robin(self, strategies: List[Strategy], rounds: int) -> GameResult:
        result = GameResult()
        for i in range(len(strategies)):
            for j in range(i + 1, len(strategies)):
                result.combine(self.play_single_game(strategies[i], strategies[j], rounds))

        return result
