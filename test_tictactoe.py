import pytest
from tictactoe import get_winner
from tictactoe import Player
from tictactoe import validate_user_input

"""
Class for parameters to be used for testing user input validation
"""
class TicTacToeUserInputValidTest:
  def __init__(self, grid, row, column, expected_is_valid):
    self.grid = grid
    self.row = row
    self.column = column
    self.expected_is_valid = expected_is_valid

test_valid_user_input__valid = TicTacToeUserInputValidTest([
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
  ],
  0,
  0,
  True
)

test_valid_user_input__occupied = TicTacToeUserInputValidTest([
    [Player.PLAYER_ONE,  Player.PLAYER_NONE, Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
  ],
  0,
  0,
  False
)

test_valid_user_input__out_of_bounds = TicTacToeUserInputValidTest([
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
  ],
  3,
  3,
  False
)

test_valid_user_input__negative_value = TicTacToeUserInputValidTest([
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
  ],
  -1,
  -1,
  False
)

test_valid_user_input__string = TicTacToeUserInputValidTest([
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
  ],
  'a',
  'a',
  False
)

test_valid_user_input_list = [
  ( test_valid_user_input__valid.grid,
    test_valid_user_input__valid.row,
    test_valid_user_input__valid.column,
    test_valid_user_input__valid.expected_is_valid
  ),
  ( test_valid_user_input__occupied.grid,
    test_valid_user_input__occupied.row,
    test_valid_user_input__occupied.column,
    test_valid_user_input__occupied.expected_is_valid
  ),
  ( test_valid_user_input__negative_value.grid,
    test_valid_user_input__negative_value.row,
    test_valid_user_input__negative_value.column,
    test_valid_user_input__negative_value.expected_is_valid
  ),
  ( test_valid_user_input__string.grid,
    test_valid_user_input__string.row,
    test_valid_user_input__string.column,
    test_valid_user_input__string.expected_is_valid
  ),  
]


"""
Class for parameters to be used for testing winner check
"""
class TicTacToeWinnerTest:
  def __init__(self, grid, expected_winner):
    self.grid = grid
    self.expected_winner = expected_winner

test_row_win_1 = TicTacToeWinnerTest([
    [Player.PLAYER_ONE,  Player.PLAYER_ONE,  Player.PLAYER_ONE],
    [Player.PLAYER_TWO,  Player.PLAYER_TWO,  Player.PLAYER_ONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
  ],
  Player.PLAYER_ONE
)

test_row_win_2 = TicTacToeWinnerTest([
    [Player.PLAYER_TWO,  Player.PLAYER_TWO,  Player.PLAYER_TWO],
    [Player.PLAYER_ONE,  Player.PLAYER_ONE,  Player.PLAYER_TWO],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
  ],
  Player.PLAYER_TWO
)

test_row_win_3 = TicTacToeWinnerTest([
    [Player.PLAYER_ONE,  Player.PLAYER_TWO,  Player.PLAYER_ONE],
    [Player.PLAYER_TWO,  Player.PLAYER_TWO,  Player.PLAYER_TWO],
    [Player.PLAYER_ONE,  Player.PLAYER_ONE,  Player.PLAYER_NONE],
  ],
  Player.PLAYER_TWO
)

test_row_win_4 = TicTacToeWinnerTest([
    [Player.PLAYER_TWO,  Player.PLAYER_ONE,  Player.PLAYER_TWO],
    [Player.PLAYER_ONE,  Player.PLAYER_ONE,  Player.PLAYER_ONE],
    [Player.PLAYER_TWO,  Player.PLAYER_TWO,  Player.PLAYER_NONE],
  ],
  Player.PLAYER_ONE
)

test_column_win_1 = TicTacToeWinnerTest([
    [Player.PLAYER_ONE,  Player.PLAYER_ONE,  Player.PLAYER_TWO],
    [Player.PLAYER_ONE,  Player.PLAYER_TWO,  Player.PLAYER_TWO],
    [Player.PLAYER_ONE,  Player.PLAYER_TWO,  Player.PLAYER_NONE],
  ],
  Player.PLAYER_ONE
)

test_column_win_2 = TicTacToeWinnerTest([
    [Player.PLAYER_TWO,  Player.PLAYER_TWO,  Player.PLAYER_ONE],
    [Player.PLAYER_TWO,  Player.PLAYER_TWO,  Player.PLAYER_ONE],
    [Player.PLAYER_TWO,  Player.PLAYER_ONE,  Player.PLAYER_NONE],
  ],
  Player.PLAYER_TWO
)

test_column_win_3 = TicTacToeWinnerTest([
    [Player.PLAYER_NONE, Player.PLAYER_TWO,  Player.PLAYER_ONE],
    [Player.PLAYER_NONE, Player.PLAYER_TWO,  Player.PLAYER_ONE],
    [Player.PLAYER_ONE,  Player.PLAYER_TWO,  Player.PLAYER_NONE],
  ],
  Player.PLAYER_TWO
)

test_column_win_4 = TicTacToeWinnerTest([
    [Player.PLAYER_NONE, Player.PLAYER_ONE,  Player.PLAYER_TWO],
    [Player.PLAYER_NONE, Player.PLAYER_ONE,  Player.PLAYER_TWO],
    [Player.PLAYER_TWO,  Player.PLAYER_ONE,  Player.PLAYER_NONE],
  ],
  Player.PLAYER_ONE
)

test_diag_win_1 = TicTacToeWinnerTest([
    [Player.PLAYER_ONE,  Player.PLAYER_TWO,  Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_ONE,  Player.PLAYER_TWO],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_ONE],
  ],
  Player.PLAYER_ONE
)

test_diag_win_2 = TicTacToeWinnerTest([
    [Player.PLAYER_TWO,  Player.PLAYER_ONE,  Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_TWO,  Player.PLAYER_ONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_TWO],
  ],
  Player.PLAYER_TWO
)

test_diag_win_3 = TicTacToeWinnerTest([
    [Player.PLAYER_TWO,  Player.PLAYER_TWO,  Player.PLAYER_ONE],
    [Player.PLAYER_NONE, Player.PLAYER_ONE,  Player.PLAYER_TWO],
    [Player.PLAYER_ONE,  Player.PLAYER_NONE, Player.PLAYER_TWO],
  ],
  Player.PLAYER_ONE
)

test_diag_win_4 = TicTacToeWinnerTest([
    [Player.PLAYER_ONE,  Player.PLAYER_ONE,  Player.PLAYER_TWO],
    [Player.PLAYER_NONE, Player.PLAYER_TWO,  Player.PLAYER_ONE],
    [Player.PLAYER_TWO,  Player.PLAYER_NONE, Player.PLAYER_ONE],
  ],
  Player.PLAYER_TWO
)

test_no_winner_1 = TicTacToeWinnerTest([
    [Player.PLAYER_TWO,  Player.PLAYER_ONE,  Player.PLAYER_TWO],
    [Player.PLAYER_ONE,  Player.PLAYER_NONE, Player.PLAYER_ONE],
    [Player.PLAYER_TWO,  Player.PLAYER_TWO,  Player.PLAYER_NONE],
  ],
  Player.PLAYER_NONE
)

test_no_winner_2 = TicTacToeWinnerTest([
    [Player.PLAYER_NONE,  Player.PLAYER_ONE,  Player.PLAYER_TWO],
    [Player.PLAYER_ONE,  Player.PLAYER_NONE, Player.PLAYER_ONE],
    [Player.PLAYER_TWO,  Player.PLAYER_TWO,  Player.PLAYER_NONE],
  ],
  Player.PLAYER_NONE
)

test_no_winner_3 = TicTacToeWinnerTest([
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_NONE],
  ],
  Player.PLAYER_NONE
)

test_no_winner_4 = TicTacToeWinnerTest([
    [Player.PLAYER_ONE,  Player.PLAYER_TWO,  Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_TWO,  Player.PLAYER_NONE],
    [Player.PLAYER_NONE, Player.PLAYER_NONE, Player.PLAYER_ONE],
  ],
  Player.PLAYER_NONE
)

test_row_win_list = [
  (test_row_win_1.grid, test_row_win_1.expected_winner),
  (test_row_win_2.grid, test_row_win_2.expected_winner),
  (test_row_win_3.grid, test_row_win_3.expected_winner),
  (test_row_win_4.grid, test_row_win_4.expected_winner),
]

test_column_win_list = [
  (test_column_win_1.grid, test_column_win_1.expected_winner),
  (test_column_win_2.grid, test_column_win_2.expected_winner),
  (test_column_win_3.grid, test_column_win_3.expected_winner),
  (test_column_win_4.grid, test_column_win_4.expected_winner),
]

test_diag_win_list = [
  (test_diag_win_1.grid, test_diag_win_1.expected_winner),
  (test_diag_win_2.grid, test_diag_win_2.expected_winner),
  (test_diag_win_3.grid, test_diag_win_3.expected_winner),
  (test_diag_win_4.grid, test_diag_win_4.expected_winner),
]

test_no_winner_list = [
  (test_no_winner_1.grid, test_no_winner_1.expected_winner),
  (test_no_winner_2.grid, test_no_winner_2.expected_winner),
  (test_no_winner_3.grid, test_no_winner_3.expected_winner),
  (test_no_winner_4.grid, test_no_winner_4.expected_winner),
]


"""
Functions to run unit tests
"""

@pytest.mark.parametrize('grid, row, column, expected_is_valid', test_valid_user_input_list)
def test_validate_input(grid, row, column, expected_is_valid):
  actual_is_valid = validate_user_input(grid, row, column)
  assert actual_is_valid == expected_is_valid

@pytest.mark.parametrize('grid, expected_winner', test_row_win_list)
def test_get_winner__rows(grid, expected_winner):
  actual_winner = get_winner(grid)
  assert actual_winner == expected_winner


@pytest.mark.parametrize('grid, expected_winner', test_column_win_list)
def test_get_winner__columns(grid, expected_winner):
  actual_winner = get_winner(grid)
  assert actual_winner == expected_winner

@pytest.mark.parametrize('grid, expected_winner', test_diag_win_list)
def test_get_winner__diag(grid, expected_winner):
  actual_winner = get_winner(grid)
  assert actual_winner == expected_winner

@pytest.mark.parametrize('grid, expected_winner', test_no_winner_list)
def test_get_winner__no_winner(grid, expected_winner):
  actual_winner = get_winner(grid)
  assert actual_winner == expected_winner

