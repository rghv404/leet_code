'''
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
'''

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [['_' for _ in range(n)] for _ in range(n)]
        print(self.board)

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        #populate board
        self.board[row][col] = 'X' if player == 1 else 'O'
        #check if anyone wins
        currVal,n = self.board[row][col], len(self.board)
        if all(self.board[row][i] == currVal for i in range(n)) \
        or all(self.board[i][col] == currVal for i in range(n)) \
        or all(self.board[i][i] == currVal for i in range(n)) \
        or all(self.board[i][n-1-i] == currVal for i in range(n)):
            return player
        print(self.board)
        return 0
 n
toe = TicTacToe(3)
print(toe.move(0,0,1))
print(toe.move(0, 2, 2))
print(toe.move(2, 2, 1))
# print(toe.move(1, 1, 2))
# print(toe.move(2, 0, 1))
# print(toe.move(1, 0, 2))
# print(toe.move(2, 1, 1))
toe2 = TicTacToe(2)
print(toe2.move(0,1,1))
print(toe2.move(1, 1, 2))
print(toe2.move(1, 0, 1))