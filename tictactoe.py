from __future__ import print_function
import sys
import re

DEFAULT_SIZE = 3
EMPTY =  ' '

def parse_user_input(board, user_input):
	mark = None
	ret_val = None
	valid_input = False

	print(user_input)
	pattern = re.compile('^([0-9])*,([0-9])*$')
	
	if (pattern.match(user_input)):
		mark = [int(x) for x in user_input.split(',')]
	else:
		print('Invalid format')

	is_in_bounds = ((mark != None) and
		            (mark[0] < len(board) and mark[1] < len(board)))
	is_not_occupied = ((mark != None) and
		               is_in_bounds and 
		               board[mark[0]][mark[1]] == EMPTY)

	if (is_in_bounds and is_not_occupied):
		ret_val = mark
	else:
		if (not is_in_bounds):
			print('Out of bounds')
		if (not is_not_occupied):
			print('Location occupied')
	return ret_val

def mark_board(board, location, player):
	user_symbol = EMPTY
	if (player % 2 == 0):
		user_symbol = 'x'
	else:
		user_symbol = 'o'

	board[location[0]][location[1]] = user_symbol


def get_user_input(board, player):
	print('Player ', player, ' turn')
	print('Please indicate where you want to place your mark.')
	user_input = raw_input('Please use format "x,y": ')
	ret_val = parse_user_input(board, user_input)
	
	while (ret_val == None):
		user_input = raw_input('Invalid input. Please use format "x,y": ')
		ret_val = parse_user_input(board, user_input)
	
	return ret_val

def print_board(board):
	sys.stdout.write('\033[H')  # move to the top
	sys.stdout.write('\033[J')  # clear the screen

	for i in xrange(len(board)):
		row = ''
		for j in xrange(len(board[i])):
			row = row + board[i][j]
			#vertical border
			if j < len(board[i])-1:
				row = row + '|'
		print(row)
		#horizontal border
		if i < len(board)-1:
			row = '-'*len(row)
			print(row)

def init_board(size):
	board = [' '] * size
	for i in xrange(size):
		board[i] = [' '] * size
	return board

def main(size):
	counter = 0
	game_over = False
	board = init_board(size)
	pattern = re.compile('1')

	while (counter < size*size and
		   game_over == False):
		print_board(board)
		location = get_user_input(board, counter%2)
		mark_board(board, location, counter%2)
		counter += 1

if __name__ == '__main__':
    main(DEFAULT_SIZE)