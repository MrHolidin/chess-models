from Player import Player
from PositionEstimators import PositionEstimator
from chess import Board, Move
import chess
import typing as tp


class AlphaBetaPlayer(Player):
    def __init__(self, estimator: PositionEstimator, depth: int = 4):
        if depth <= 0:
            raise ValueError("Deep for AlphaBetaPlayer can't be lower than 0")
        self.depth = depth
        self.estimator = estimator
        self.estimation_cache = {}

    def _best_value_with_move(
        self, board: Board, depth: int, alpha: float, beta: float
    ) -> tp.Tuple[float, Move]:
        if depth == 0 or board.is_game_over():
            hsh = hash(board.fen())
            if not hsh in self.estimation_cache:
                self.estimation_cache[hsh] = self.estimator(board) * (
                    1 if board.turn == chess.WHITE else -1
                )
            return self.estimation_cache[hsh], Move.null()

        best_move = Move.null()
        if board.turn == chess.WHITE:
            best_value = float("-inf")
            for move in board.legal_moves:
                board.push(move)
                value, _ = self._best_value_with_move(board, depth - 1, alpha, beta)
                board.pop()
                if value > best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, best_value)
                if alpha >= beta:
                    break
            return best_value, best_move
        else:
            best_value = float("inf")
            for move in board.legal_moves:
                board.push(move)
                value, _ = self._best_value_with_move(board, depth - 1, alpha, beta)
                board.pop()
                if value < best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, best_value)
                if alpha >= beta:
                    break
            return best_value, best_move

    def get_next_move(self, board: Board):
        _, move = self._best_value_with_move(
            board, self.depth, float("-inf"), float("inf")
        )
        assert move
        return move
