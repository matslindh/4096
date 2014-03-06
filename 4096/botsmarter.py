#!/usr/bin/env python3
from bothelper import read_board, up, down, left, right, botsetup, rotate_board, merge_count

# register name
s = botsetup("smarter-example")

while True:
	board, score = read_board(s)

	best = 0
	best_dir = down
	best_score = 0
	dirs = [down, left, up, right]

	for d in dirs:
		c, score = merge_count(board)

		if c > best: #or (c == best and score > best_score):
			best_dir = d
			best_score = score
			best = c

		board = rotate_board(board, 1)

	best_dir(s)