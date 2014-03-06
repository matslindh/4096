#!/usr/bin/env python3
import random
from bothelper import read_board, up, down, left, right, botsetup

s = botsetup("random-example")

previous_score = 0

while True:
	board = read_board(s)
	direction = random.randint(1, 4)

	if direction == 1:
		up(s)
	elif direction == 2:
		down(s)
	elif direction == 3:
		left(s)
	else:
		right(s)