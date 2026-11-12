# HW 3: Game AI

**Due Wednesday, November 11 at 11:00 pm.**

## The Premise

After you sold your unicorn ChowRider, you used your massive windfall to travel the world eating exclusively at Michelin-starred restaurants, then settled down in a modest, 20-room mansion in Winnetka, right on the lake just north of Evanston. One gloomy morning, staring out your floor-to-ceiling window, you realized that for a bored billionaire who had everything, one thing was missing. (No, not the Continuum Transfunctioner. You have that too.) Your lush lawn between the house and your private beach needs an 8x8 chess/checkers board with humongous pieces, like the one Ron Weasley played on in *Harry Potter and the Sorcerer's Stone*. Three business days later, you had that too.

Now you just need to invite a former Intro to AI classmate from Northwestern over to play. Chess isn't one of your undeniable talents, so it's checkers. But mischief has gotten the better of you: you want your recently acquired brain implant to receive the best moves from an innocent little Mac upstairs in your study. You could buy the best checkers AI out there, but you're a bored billionaire, and you miss that marvelous course with the most amazing professor (so modest he'd never call himself amazing), so you'll write your own using the adversarial search you learned there: Minimax, first plain and then with Alpha-Beta Pruning, so you can see what pruning buys you.

Your buddies at TestFriendForever (TFF) supply a codebase, a test suite, and some secret tests they'll run before awarding your code a gold star.

## Overview

Implement three functions in `ai.py`, the only file you edit and submit. Do them in order: Parts 2 and 3 score boards with `evaluate()`, which calls your `counts()`, so the search tests can't pass locally until Part 1 does.

| Part | Function | Task |
| --- | --- | --- |
| 1 | `counts()` | Count one player's pieces, kings, moves, capture opportunities and king hopefuls. `evaluate()` combines them into a score. |
| 2 | `minimax()` | Minimax with **no** pruning. |
| 3 | `minimax_alpha_beta()` | Minimax with Alpha-Beta pruning: same answers as Part 2, less work. |

Then run `python compare.py` (ungraded) to see what pruning saves.

## Files

| File | Contents | Edit? |
| --- | --- | --- |
| `ai.py` | Your three functions, plus `evaluate()` and `compare_boards()` | **Yes (only this one)** |
| `test_ai.py` | Tests | No |
| `compare.py` | Minimax vs. Alpha-Beta node counts and times | No |
| `main.py` | Play against your AI in a window | No |
| `game.py` | Game rules, including `generate_all_moves()` | No |
| `board.py`, `piece.py`, `move_node.py` | `Board`, `Piece`, and a tree node used by `game.py` | No |
| `board_configs.py` | Test boards 1–28 | Only to add your own boards after 28 |
| `constants.py`, `display.py`, `crown.png` | Colors, sizes, drawing | No |
| `Boards.docx` | Pictures of boards 1–12 | — |
| `requirements.txt` | `pygame` | — |

## Setup

Python 3.9+. Install `pygame` (only `main.py` needs it; the tests need neither it nor a display), and run everything from inside this folder, since files are found by relative path:

```
pip install -r requirements.txt
cd "HW 3"
python test_ai.py
```

## How the game is represented

- **Board:** 8x8; row 0 is the top, column 0 the left. `board.get_piece(row, col)` returns `0` (empty) or a `Piece`; `board.get_all_pieces(color)` returns one player's pieces.
- **Piece:** has `row`, `col`, `color`, `king` (bool). Compare colors with `PLAYER1_PIECE_COLOR` / `PLAYER2_PIECE_COLOR` (already imported in `ai.py`).
- **Board configurations:** `board_configs.py` writes boards as 8 lists of 8 numbers: `0` empty, `1`/`11` Player 1 piece/king, `2`/`22` Player 2 piece/king. `Board(board_configs.board_config4)` builds one; `Board()` is the opening position.
- **Moves:** `game.generate_all_moves(board, color)` returns a list of new `Board`s, one per legal move, already played out (including multi-jump captures and promotion). It never modifies the board you pass in. In the search, a move *is* the board after it.

| | Player 1 | Player 2 |
| --- | --- | --- |
| Who | You (human), light | The AI, dark |
| Starts on | rows 5–7 | rows 0–2 |
| Regular pieces move | toward row 0 | toward row 7 |
| Kinged on | row 0 | row 7 |
| In the search | **minimizing** | **maximizing** |

Kings move diagonally in all four directions. `evaluate()` scores from Player 2's view: higher is better for the AI.

## Part 1: `counts(board, game, color)`

Return five ints for that player, in this order:

1. `num_pieces`: pieces on the board, kings included
2. `num_kings`
3. `num_moves`: single-hop moves over all their pieces
4. `num_opportunities`: how many of those moves are captures
5. `num_king_hopefuls`: how many of those moves would promote a regular piece

Don't modify `evaluate()`; it calls `counts()` once per player and weights the differences.

**What counts as a move.** For each piece and each direction it may move (two forward for a regular piece, four for a king), look at the diagonally adjacent square:

- **Empty:** one move.
- **Opponent's piece:** if the next square beyond it in the same direction is on the board and empty, one move **and** one capture; otherwise nothing.
- **Off the board or your own piece:** nothing.

Count **single hops only**: ignore multi-jumps, even though real checkers and `game.py` allow them. So don't use `game.find_moves()` or `game.generate_all_moves()` here; they include multi-jumps and won't match the tests.

A **king hopeful** is a move by a non-king that ends on its far row (row 0 for Player 1, row 7 for Player 2), captures included. A piece with two such moves counts twice.

**Worked examples** (test boards):

- **Board 4, Player 1 → `(1, 1, 0, 0, 0)`.** One king at (7, 4). Its upward neighbors (6, 3) and (6, 5) are Player 2 pieces with occupied squares beyond them, (5, 2) and (5, 6), so no captures; downward is off the board.
- **Board 5, Player 1 → `(1, 1, 1, 1, 0)`.** Same as board 4 but (5, 2) is empty, so the king can capture (6, 3) by jumping to (5, 2).
- **Board 4, Player 2: 2 king hopefuls.** (6, 3) can step to the empty (7, 2); its other forward square (7, 4) holds the Player 1 king, and jumping it leaves the board. (6, 5) can step to the empty (7, 6).

## Part 2: `minimax(board, depth, max_player, game, eval_params=None)`

Minimax with no pruning: look `depth` plies ahead (a ply is one player's move), assume both sides play their best, and return `(score, best_move)` for whoever's turn it is.

- `max_player`: `True` on Player 2's (the AI's) turn, `False` on Player 1's.
- `eval_params`: `None`, or five weights in `evaluate()`'s argument order `(pieces, kings, moves, opportunities, king_hopefuls)`. Call `evaluate(board, game, *eval_params)`, or `evaluate(board, game)` when it's `None`. Pass it unchanged to recursive calls.
- `score`: the minimax value of `board`.
- `best_move`: the board after the best move available **now**, i.e. one of the boards `generate_all_moves()` returned for *this* board, not a deeper one. With no move to make (depth 0, or no moves), return `board`.

Follow the **search rules** below exactly; the tests check the exact move, score and number of boards expanded (calls to `generate_all_moves()`). Plain Minimax must expand every board in the tree exactly once, which rules S1 and S2 guarantee.

## Part 3: `minimax_alpha_beta(board, depth, alpha, beta, max_player, game, eval_params=None)`

The same search with Alpha-Beta pruning. It must return **exactly** `minimax()`'s score and move while expanding fewer boards. `alpha` and `beta` are the best scores the maximizer and minimizer are already guaranteed elsewhere in the tree; start with `float('-inf')` and `float('inf')`, and pass the current values to each recursive call. Rules S1–S6 apply.

The tests require fewer boards than the full tree wherever pruning is possible, but no exact count, so how you organize the code is up to you.

> **Why `<=` and not `<` (S6)?** Both are correct Alpha-Beta and return the same answer as Minimax; textbooks use both. We picked `<=` only so pruning can be tested: many moves here tie, `<` never prunes on a tie, and on a couple of test positions a correct `<` search expands exactly as many boards as plain Minimax. It's a convention for this assignment, not a claim that `<` is wrong.

## Search rules

- **S1. Depth 0:** if `depth == 0`, return `(evaluate(...), board)` immediately, without generating moves.
- **S2. Generate once:** otherwise call `game.generate_all_moves(board, color)` exactly once, with `PLAYER2_PIECE_COLOR` if `max_player` else `PLAYER1_PIECE_COLOR`.
- **S3. No moves is a loss:** if that list is empty (including no pieces left), return `float('-inf')` if `max_player` else `float('inf')`, without calling `evaluate()`.
- **S4. Order:** try moves in the order returned, each with `depth - 1` and `not max_player`.
- **S5. Ties keep the first:** replace your best move only when a later one is *strictly* better (higher for the maximizer, lower for the minimizer).
- **S6. Pruning (Part 3 only):** after each move, update `alpha = max(alpha, score)` on the maximizer's turn or `beta = min(beta, score)` on the minimizer's; then if `beta <= alpha`, stop and return the best so far.

## Running and comparing

```
python test_ai.py                                everything (~10 s with a working solution)
python test_ai.py CountsTest                     Part 1  (also MinimaxTest, AlphaBetaTest)
python test_ai.py MinimaxTest.test_minimax_08    one test
python compare.py                                opening position, depths 1-5
python compare.py --board 2 --max-depth 6        another board, deeper (plain Minimax ~30 s at 6)
python main.py                                   play Alpha-Beta at depth 3
python main.py --search minimax --depth 4        play plain Minimax: feel the wait
```

| Class | Tests | Checks |
| --- | --- | --- |
| `CountsTest` | `test_counts`, `test_evaluate_1`–`_4` | `counts()` on boards 1–6; `evaluate()` on boards 1–12 with four weight sets |
| `MinimaxTest` | `test_minimax_01`–`_16` | Move and score from 16 positions, depths 1–4 |
| | `test_minimax_visits_the_whole_tree` | Exactly the full tree on each |
| `AlphaBetaTest` | `test_alpha_beta_01`–`_16` | Same 16 positions, same move and score |
| | `test_alpha_beta_prunes` | Fewer boards than the full tree wherever pruning is possible |

Failures explain themselves: a wrong move prints your board beside the expected one (in `board_configs.py` format); a count failure names the board, player and metric.

`compare.py` prints, per depth, boards expanded by each search, percent pruned, time, and whether they agree; at depth 5 a correct Alpha-Beta prunes about 80% and runs about 5× faster. In `main.py` you play light: click a piece, then a blue dot. Until you implement the search, the AI moves randomly, so hold the celebrations.

**Debugging tips**

- `board.print_board_config(board.to_board_config())` prints a board; `Display().display_board(board)` shows it in a window (close it to continue).
- Rebuild a test position with e.g. `Board(board_configs.board_config2)` and call your function at a small depth.
- Right score, wrong move: check S4 and S5; moves often tie.
- Expected score `inf`: the best line leaves Player 1 with no moves (S3).
- Minimax passes but `test_alpha_beta_prunes` fails: you're not updating `alpha`/`beta` after every move, or not using `<=` (S6).

## Rules

1. Implement all three functions in `ai.py`.
2. Edit no other file, except to add boards after 28 in `board_configs.py`. We grade with fresh copies of every other file.
3. Add any helpers you like, but don't change `evaluate()`, `compare_boards()`, or the three functions' names and arguments.
4. Any standard Python module is fine, but nothing that implements Minimax or Alpha-Beta for you.

## Grading

10 points: Part 1 is worth 1, Part 2 is worth 4, Part 3 is worth 5. We grade with `test_ai.py` plus hidden tests built the same way on other boards, so passing locally is a good sign, not a guarantee. Within Parts 2 and 3, each position is worth 70% for the right move and score and 30% for the node count (the full tree for Minimax, pruning for Alpha-Beta); the node-count share is earned only where the move and score are also right. Parts are graded separately, and Parts 2 and 3 use a correct `counts()` in place of yours, so a Part 1 mistake costs only Part 1.

## Submission

Submit only `ai.py`, zipped as `netid_hw3.zip` in lowercase with your netid, e.g. `abc1234_hw3.zip`. When resubmitting, rename browser duplicates like `abc1234_hw3 1.zip` back to exactly that name.
