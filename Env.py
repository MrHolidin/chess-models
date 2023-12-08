import chess
from chess import Board, Move
from Player import Player


class GameEnv:
    def __init__(
        self, player_white: Player, player_black: Player, max_turns: int | None = None
    ):
        self.player_white = player_white
        self.player_black = player_black
        self.max_turns = max_turns
        self.board = Board()

    def play(self):
        self.board.reset()
        while self.board.outcome() is None:
            if self.board.fullmove_number == self.max_turns:
                break
            if self.board.turn == chess.WHITE:
                move = self.player_white.get_next_move(self.board)
            else:
                move = self.player_black.get_next_move(self.board)
            assert move, "You can't do nothing in chess"
            self.board.push(move)
        print("Game Over")
        print("Result: ", self.board.result())
