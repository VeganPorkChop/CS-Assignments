# HW 2: Constraint Satisfaction

Write a sudoku solver two ways and report how much work each one does. The full
task description is in `Homework Project 2.pdf`; read it first. This file only
covers how to run and submit the code.

## What you edit

`student_code.py`, and nothing else. Fill in `sudoku_backtracking` and
`sudoku_forwardchecking`. Leave `main.py` and `common.py` alone — we replace
both with fresh copies when we grade, so changes there are discarded.

Your code runs on Python 3 and may not import anything beyond `common`.

## Setup and running the tests

There are no packages to install, so any Python 3 works: conda, a virtual
environment, or whatever `python3` already points at.

Run from inside this folder, since the files find each other by relative path:

```
cd "CS348 Homework 2"
python3 main.py
```

`main.py` checks each board twice, once per function. It reports whether the
finished board is a legal sudoku that still has all of its original clues, and
whether your count matches the expected one. It exits 0 only when every board
passes both functions.

## Counting

Count every call to your recursive solver, including the first one. A board
that arrives already solved therefore reports 1, not 0.

## Grading

We grade with a different set of boards than the six in `main.py`, so passing
all six is a good sign but not a guarantee. The two functions are scored
independently — a correct `sudoku_backtracking` earns its credit even if
`sudoku_forwardchecking` is wrong.

## What to submit

A zip of your code, named `netid_hw2.zip`, all lowercase, using your own netid:

```
abc1234_hw2.zip
```

If you resubmit, make sure the file you upload is still named exactly that.
Browsers rename repeat downloads to things like `abc1234_hw2 1.zip`; rename it
back before uploading.
