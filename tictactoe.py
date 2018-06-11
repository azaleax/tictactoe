from random import randint

class Player:
  PLAYER_NONE = 0
  PLAYER_ONE  = 1
  PLAYER_TWO  = 2

SYMBOLS = {
  Player.PLAYER_NONE: ' ',
  Player.PLAYER_ONE:  'X',
  Player.PLAYER_TWO:  'O',
}

VALUES  = {
  Player.PLAYER_NONE: 0,
  Player.PLAYER_ONE:  1,
  Player.PLAYER_TWO: -1,
}

GRID_SIZE = 3

def generate_ai_input(grid):
  row    = randint(0, GRID_SIZE-1)
  column = randint(0, GRID_SIZE-1)

  square = grid[row][column]

  while (square != Player.PLAYER_NONE):
    row    = randint(0, GRID_SIZE-1)
    column = randint(0, GRID_SIZE-1)

    square = grid[row][column]

  return (row, column)


def init_grid(size):
  return [[Player.PLAYER_NONE for x in range(size)] for y in range(size)]


def print_grid(grid):
  for row in grid:
    print '|',
    for column in row:
      print SYMBOLS[column] + '|',
    print


def mark_grid(grid, user_id, row, column):
  grid[row][column] = user_id


def get_current_user_id(turn):
  return Player.PLAYER_ONE if (turn % 2 == 0) else Player.PLAYER_TWO


def validate_user_input(grid, row, column):

  try:
    is_valid = (row    in range(GRID_SIZE) and
                column in range(GRID_SIZE) and
                grid[row][column] == Player.PLAYER_NONE)

  except TypeError:
    is_valid = False

  return is_valid

def get_prompted_user_input(grid, current_user):
  print("user " + str(current_user) + "'s turn")

  try:
    raw_row    = raw_input("row: ")
    raw_column = raw_input("column: ")
    row    = int(raw_row)
    column = int(raw_column)
  
  except:
    row    = -1
    column = -1
  
  return (row, column)

def get_validated_user_input(grid, current_user):
  (row, column) = get_prompted_user_input(grid, current_user)
  
  while(validate_user_input(grid, row, column) == False):
    print("Invalid input. Try again.")
    (row, column) = get_prompted_user_input(grid, current_user)


  return (row, column)


def get_row_winner(grid):
  winner = Player.PLAYER_NONE

  for row in range(GRID_SIZE):
    row_sum = sum(VALUES[grid[row][column]] for column in range(GRID_SIZE))

    if row_sum == GRID_SIZE * VALUES[Player.PLAYER_ONE]:
      winner = Player.PLAYER_ONE
      break

    elif row_sum == GRID_SIZE * VALUES[Player.PLAYER_TWO]:
      winner = Player.PLAYER_TWO
      break

    row_sum = 0

  return winner


def get_column_winner(grid):
  winner = Player.PLAYER_NONE

  for column in range(GRID_SIZE):
    column_sum = sum(VALUES[grid[row][column]] for row in range(GRID_SIZE))

    if column_sum == GRID_SIZE * VALUES[Player.PLAYER_ONE]:
      winner = Player.PLAYER_ONE
      break

    elif column_sum == GRID_SIZE * VALUES[Player.PLAYER_TWO]:
      winner = Player.PLAYER_TWO
      break

    column_sum = 0

  return winner


def get_diag_winner(grid):
  winner = Player.PLAYER_NONE

  forward_diag_sum  = sum(VALUES[grid[index][index]] for index in range(GRID_SIZE))
  backward_diag_sum = sum(VALUES[grid[index][(GRID_SIZE - 1) - index]] for index in range(GRID_SIZE))
  
  if (forward_diag_sum  == GRID_SIZE * VALUES[Player.PLAYER_ONE] or
      backward_diag_sum == GRID_SIZE * VALUES[Player.PLAYER_ONE]):
    winner = Player.PLAYER_ONE

  elif (forward_diag_sum  == GRID_SIZE * VALUES[Player.PLAYER_TWO] or
        backward_diag_sum == GRID_SIZE * VALUES[Player.PLAYER_TWO]):
    winner = Player.PLAYER_TWO

  return winner

def get_winner(grid):
  winner = Player.PLAYER_NONE

  winner = get_row_winner(grid)

  if winner == Player.PLAYER_NONE:
    winner = get_column_winner(grid)

  if winner == Player.PLAYER_NONE:
    winner = get_diag_winner(grid)

  return winner


if __name__ == "__main__":

  winner = Player.PLAYER_NONE
  total_possible_turns = GRID_SIZE * GRID_SIZE
  grid = init_grid(GRID_SIZE)

  print("Welcome to tictactoe!")
  print

  print_grid(grid)

  for turn in range(total_possible_turns):

    current_user = get_current_user_id(turn)

    if (current_user == Player.PLAYER_TWO):
      (row, column) = generate_ai_input(grid)
    else:
      (row, column) = get_validated_user_input(grid, current_user)

    mark_grid(grid, current_user, row, column)

    print("After turn " + str(turn) + " grid updated")
  
    print_grid(grid)

    winner = get_winner(grid)

    if winner != Player.PLAYER_NONE:
      print("Congratulations!")
      print("user " + str(current_user) + " has won!")
      break

  if winner != Player.PLAYER_NONE:
    print("Game ended in a tie")