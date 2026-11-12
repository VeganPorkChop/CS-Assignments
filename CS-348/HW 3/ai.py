"""HW 3: Game AI. This is the only file you edit and submit.

You implement three functions, marked TO DO below:

    counts()              Part 1: the metrics that evaluate() combines into a score
    minimax()             Part 2: Minimax, with no pruning
    minimax_alpha_beta()  Part 3: Minimax with Alpha-Beta pruning

Read README.md first. Its search rules S1-S6 are repeated in the docstrings below.

Run the tests with:    python test_ai.py
Compare the searches:  python compare.py
"""
from board import Board
from constants import PLAYER1_PIECE_COLOR, PLAYER2_PIECE_COLOR
import random
    
# TO DO (Part 2): Implement this function. The three lines currently in it pick a random move so that main.py works
# before you start. Replace all of them with your own code.
def minimax(board, depth, max_player, game, eval_params=None):
    """
    Minimax WITHOUT pruning: the best move for the player whose turn it is, searching depth plies ahead.

    Args:
        board (Board): Current board. Don't modify it; game.generate_all_moves() returns new boards.
        depth (int): Plies (single moves by one player) left to search below this board.
        max_player (bool): True on the maximizer's turn (AI, Player 2, dark), False on the minimizer's
            (human, Player 1, light).
        game (Game): Use its generate_all_moves(), and pass it to evaluate().
        eval_params (tuple or None): Weights for evaluate(), in its argument order (pieces, kings, moves,
            opportunities, king_hopefuls): call evaluate(board, game, *eval_params), or evaluate(board, game)
            if None. Pass it unchanged to recursive calls.

    Returns:
        (score, best_move): the minimax value of board, and the board after the best move available NOW (one of
        the boards generate_all_moves() returned for this board, not a deeper one). With no move to make
        (depth 0, or no moves), best_move is board itself.

    Rules (the tests check the exact score, move and number of generate_all_moves() calls):
        S1. depth == 0: return (evaluate(...), board) without generating moves.
        S2. Otherwise call game.generate_all_moves(board, color) exactly once, color = PLAYER2_PIECE_COLOR if
            max_player else PLAYER1_PIECE_COLOR.
        S3. No moves (including no pieces) means that player lost: score float('-inf') if max_player else
            float('inf'), without calling evaluate().
        S4. Try moves in the order returned, each with depth - 1 and not max_player.
        S5. On a tie keep the move found first: replace the best only when a later move is strictly better.
    """

    if depth == 0:
        return evaluate(board, game, *(eval_params or ())), board
 
    color = PLAYER2_PIECE_COLOR if max_player else PLAYER1_PIECE_COLOR
    moves = game.generate_all_moves(board, color)
    if not moves:
        return float('-inf') if max_player else float('inf'), board
 
    best_score = float('-inf') if max_player else float('inf')
    best_move = moves[0]
    for move in moves:
        score, _ = minimax(move, depth - 1, not max_player, game, eval_params)
        if (max_player and score > best_score) or (not max_player and score < best_score):
            best_score = score
            best_move = move
 
    return best_score, best_move


# TO DO (Part 3): Implement this function. The three lines currently in it pick a random move so that main.py works
# before you start. Replace all of them with your own code.
def minimax_alpha_beta(board, depth, alpha, beta, max_player, game, eval_params=None):
    """
    Minimax WITH Alpha-Beta pruning. Must return exactly minimax()'s score and move for the same arguments,
    while expanding fewer boards.

    Args:
        alpha (float): Best score the maximizer is already guaranteed elsewhere in the tree; start at float('-inf').
        beta (float): Same for the minimizer; start at float('inf').
        Pass the current alpha and beta to recursive calls. Other arguments and the return value: as in minimax().

    Rules: S1-S5 of minimax(), plus
        S6. After each move, alpha = max(alpha, score) on the maximizer's turn, beta = min(beta, score) on the
            minimizer's; then if beta <= alpha, stop and return the best so far. (beta < alpha is also correct
            Alpha-Beta; we use <= so the tests can see pruning when moves tie. See "Why <= and not <?" in README.md.)
    """

    if depth == 0:
        return evaluate(board, game, *(eval_params or ())), board

    color = PLAYER2_PIECE_COLOR if max_player else PLAYER1_PIECE_COLOR
    moves = game.generate_all_moves(board, color)
    if not moves:
        return float('-inf') if max_player else float('inf'), board

    best_score = float('-inf') if max_player else float('inf')
    best_move = moves[0]
    for move in moves:
        score, _ = minimax_alpha_beta(move, depth - 1, alpha, beta, not max_player, game, eval_params)
        if (max_player and score > best_score) or (not max_player and score < best_score):
            best_score = score
            best_move = move

        if max_player:
            alpha = max(alpha, best_score)
        else:
            beta = min(beta, best_score)

        if beta <= alpha:
            break

    return best_score, best_move


def evaluate(board, game, pieces_weight=1.0, kings_weight=1.0, moves_weight=0.0, opportunities_weight=0.0, king_hopefuls_weight=0.0):
    """
    DO NOT MODIFY THIS FUNCTION.

    Evaluates the given board and returns a score based on a weighted combination of these metrics:

        1. The difference in the number of own pieces vs. opponent pieces
        2. The difference in the number of own kings vs. opponent kings
        3. The difference in the number of own king hopefuls vs. opponent king hopefuls (See Notes below)
        4. The difference in the number of capture opportunities for the player vs. the opponent
        5. The difference in the number of moves available for the player vs. the opponent.

    The AI player (using Minimax) is assumed to be Player 2.

    Args:
        board (Board): The current state of the game board
        game (Game): The game instance
        pieces_weight (float): Weight for the difference in piece count
        kings_weight (float): Weight for the difference in king count
        moves_weight (float): Weight for the difference in available moves
        opportunities_weight (float): Weight for the difference in capture opportunities
        king_hopefuls_weight (float): Weight for the difference in king hopefuls.

    Returns:
        float: A score representing the board's goodness for Player 2

    Notes:
        - King hopefuls have to do with pieces that can become king in the next move and are counted not just as the
        number of such pieces but as how many such king promotions can occur. So, if a piece can become king in its
        next move in two ways, then the piece is counted twice.
    """

    p1_num_pieces, p1_num_kings, p1_num_moves, p1_num_opportunities, p1_num_king_hopefuls = counts(board, game, PLAYER1_PIECE_COLOR)
    p2_num_pieces, p2_num_kings, p2_num_moves, p2_num_opportunities, p2_num_king_hopefuls = counts(board, game, PLAYER2_PIECE_COLOR)

    pieces_diff = p2_num_pieces - p1_num_pieces
    kings_diff = p2_num_kings - p1_num_kings
    moves_diff = p2_num_moves - p1_num_moves
    opportunities_diff = p2_num_opportunities - p1_num_opportunities
    king_hopefuls_diff = p2_num_king_hopefuls - p1_num_king_hopefuls

    score = (pieces_diff * pieces_weight +
             kings_diff * kings_weight +
             moves_diff * moves_weight +
             opportunities_diff * opportunities_weight +
             king_hopefuls_diff * king_hopefuls_weight)

    return score


# TO DO (Part 1): Implement this function.
def counts(board, game, color):
    """
    Metrics for the pieces of one color.

    Args:
        board (Board): Current board.
        game (Game): Not needed here; passed so the signature matches evaluate().
        color (tuple): PLAYER1_PIECE_COLOR or PLAYER2_PIECE_COLOR.

    Returns:
        Five ints, in order: num_pieces (kings included), num_kings, num_moves (single hops over all pieces),
        num_opportunities (moves that are captures), num_king_hopefuls (moves that promote a regular piece).

    What counts as a move (worked examples in README.md, Part 1):
        - Regular pieces move toward row 0 (Player 1, light) or row 7 (Player 2, dark); kings in all four diagonals.
        - For each direction, the diagonally adjacent square is:
            * empty: one move;
            * an opponent's piece with an empty, on-board square directly beyond it: one move and one capture;
            * anything else: no move.
        - Single hops only: ignore multi-jumps, and don't use game.find_moves() or game.generate_all_moves() here.
        - King hopeful: a non-king's move (captures included) ending on its far row (row 0 for Player 1, row 7 for
          Player 2). A piece with two such moves counts twice.
    """
    
    num_pieces = 0
    num_kings = 0
    num_moves = 0
    num_opportunities = 0
    num_king_hopefuls = 0
    promotion_row = 0 if color == PLAYER1_PIECE_COLOR else 7
    forward = ((-1, -1), (-1, 1)) if color == PLAYER1_PIECE_COLOR else ((1, -1), (1, 1))
    all_dirs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
 
    for row in range(8):
        for col in range(8):
            piece = board.get_piece(row, col)
            if piece == 0 or piece.color != color:
                continue
 
            num_pieces += 1
            if piece.king:
                num_kings += 1
            directions = all_dirs if piece.king else forward
 
            for row_delta, col_delta in directions:
                landing_row = row + row_delta
                landing_col = col + col_delta
                if not (0 <= landing_row < 8 and 0 <= landing_col < 8):
                    continue
 
                landing_piece = board.get_piece(landing_row, landing_col)
                if landing_piece == 0:
                    num_moves += 1
                    if not piece.king and landing_row == promotion_row:
                        num_king_hopefuls += 1
                elif landing_piece.color != color:
                    jump_row = landing_row + row_delta
                    jump_col = landing_col + col_delta
                    if (0 <= jump_row < 8 and 0 <= jump_col < 8 and
                            board.get_piece(jump_row, jump_col) == 0):
                        num_moves += 1
                        num_opportunities += 1
                        if not piece.king and jump_row == promotion_row:
                            num_king_hopefuls += 1
 
    return num_pieces, num_kings, num_moves, num_opportunities, num_king_hopefuls


def compare_boards(board1, board2):
    """
    Compares two board objects to determine if they are identical in piece layout, piece color, and piece status (king or non-king).

    Args:
        board1 (Board): The first board object to compare.
        board2 (Board): The second board object to compare.

    Returns:
        bool: True if the boards are identical in terms of piece layout, piece color, and king status at each position; False otherwise

    The function checks each position (row, col) on an 8x8 board grid:
    - If both positions are empty (denoted by 0), it continues to the next position.
    - If only one position is empty, it returns False.
    - If both positions contain a piece, it checks that the pieces have the same color and king status. If any discrepancy is found, it returns False.

    Assumptions:
        - `board1` and `board2` are expected to have a `get_piece(row, col)` method that  returns either a piece object
        (with `color` and `king` attributes) or 0 if the position is empty.
    """

    if not isinstance(board1, Board) or not isinstance(board2, Board):
        return False

    for row in range(8):
        for col in range(8):
            piece1 = board1.get_piece(row, col)
            piece2 = board2.get_piece(row, col)

            if piece1 == 0 and piece2 == 0:
                continue

            if (piece1 == 0) != (piece2 == 0):
                return False

            if piece1.color != piece2.color or piece1.king != piece2.king:
                return False

    return True
