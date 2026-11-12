"""Compare your minimax() and minimax_alpha_beta() side by side.

    python compare.py                    opening position, depths 1 to 5
    python compare.py --board 2          start from board_config2 instead
    python compare.py --max-depth 6      search deeper (plain Minimax takes about 30 seconds at depth 6)

For each depth this prints how many boards each search expanded (calls to game.generate_all_moves()), how long it
took, and whether the two searches agreed on the score and the move. They always should: Alpha-Beta pruning only
skips moves that cannot change the answer.

Nothing here is graded. It is here so you can see what pruning buys you.
"""
import argparse
import time

import board_configs
from ai import compare_boards, minimax, minimax_alpha_beta
from board import Board
from game import Game

WEIGHTS = (1.0, 1.0, 0.5, 0.5, 0.25)


class CountingGame(Game):
    def __init__(self):
        super().__init__()
        self.nodes = 0

    def generate_all_moves(self, board, color):
        self.nodes += 1
        return super().generate_all_moves(board, color)


def run(search, board_number, depth):
    board = Board() if board_number is None else Board(getattr(board_configs, 'board_config%d' % board_number))
    game = CountingGame()
    start = time.perf_counter()
    if search is minimax:
        score, move = minimax(board, depth, True, game, WEIGHTS)
    else:
        score, move = minimax_alpha_beta(board, depth, float('-inf'), float('inf'), True, game, WEIGHTS)
    return score, move, game.nodes, time.perf_counter() - start


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--board', type=int, help='board_config number to start from (default: the opening position)')
    ap.add_argument('--max-depth', type=int, default=5)
    args = ap.parse_args()

    where = 'the opening position' if args.board is None else 'board_config%d' % args.board
    print('Searching from %s for Player 2 with eval_params=%s\n' % (where, WEIGHTS))
    print('%5s  %14s  %16s  %7s  %10s  %12s  %s' % ('depth', 'minimax nodes', 'alpha-beta nodes', 'pruned',
                                                    'minimax s', 'alpha-beta s', 'same answer'))
    for depth in range(1, args.max_depth + 1):
        s1, m1, n1, t1 = run(minimax, args.board, depth)
        s2, m2, n2, t2 = run(minimax_alpha_beta, args.board, depth)
        pruned = '%6.0f%%' % (100.0 * (n1 - n2) / n1) if n1 else '      -'
        same = 'yes' if s1 == s2 and compare_boards(m1, m2) else 'NO: scores %s vs %s' % (s1, s2)
        print('%5d  %14d  %16d  %7s  %10.3f  %12.3f  %s' % (depth, n1, n2, pruned, t1, t2, same))


if __name__ == '__main__':
    main()
