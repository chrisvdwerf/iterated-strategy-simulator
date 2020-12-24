from typing import List


class Strategy:
    def get_next_move(self, previous_moves_opponent: List[int]) -> int:
        raise NotImplemented()


class TikForTat(Strategy):
    def get_next_move(self, previous_moves_opponent: List[int]) -> int:
        if len(previous_moves_opponent) == 0:
            return 1

        return previous_moves_opponent[-1]


class NonCooperative(Strategy):
    def get_next_move(self, previous_moves_opponent: List[int]) -> int:
        return 0
