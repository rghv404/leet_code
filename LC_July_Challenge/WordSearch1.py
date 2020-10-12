'''

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

 

Constraints:

    board and word consists only of lowercase and uppercase English letters.
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3



'''

# naive solution is to go through the board and once the first letter is found then start the depth first search
# Since we are only searching one word we can even modiy the visited word as # or something to avoid revisitng the word
def search(i:int, j:int, idx:int, word:str)->bool:
		if idx == len(word):
			return True

		if i > len(board)-1 or i < 0 or j > len(board[0])-1 or j < 0:
			return False

		flag = False

		if board[i][j] == word[idx]:
			board[i][j] = '#'
			flag = search(i+1, j, idx+1, word ) or search(i-1, j, idx+1, word)\
				or search(i, j+1, idx+1, word ) or search(i, j-1, idx+1, word)
			# if not flag = brd[i][j] = 
			board[i][j] = word[idx]
		return flag

def exist(board: [[str]], word: str) -> bool:
	if not word or not board:
		return False
	for i in range(len(board)):
		for j in range(len(board[0])):
			# print('Searching again: ', board)
			if betterSearch(i, j, 0, word):
				return True
	return False


# it is infact better to use a loop to do dfs rather than or cause in or condition it will go through everycase before assigning
# the flag value 

def betterSearch(i:int, j:int, idx:int, word:str)-> bool:
	if idx == len(word):
		return True

	if i > len(board)-1 or i < 0 or j > len(board[0])-1 or j < 0 or board[i][j] != word[idx]:
		return False

	flag = False
	board[i][j] = '#'
	for (rowInc, colInc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		flag = betterSearch(i+rowInc, j+colInc, idx+1, word)
		if flag: break
	board[i][j] = word[idx]
	return flag
	# backtrack to set the word to original

word = "oathh"
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["b","c","d","e"],["f","g","h","i"],["j","k","l","m"],["n","o","p","q"],["r","s","t","u"],["v","w","x","y"],["z","z","z","z"]]
word = "aaaaaaaaaaaaaaaa"

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCB"

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

board = [["F","Y","C","E","N","R","D"],
		["K","L","N","F","I","N","U"],
		["A","A","A","R","A","H","R"],
		["N","D","K","L","P","N","E"],
		["A","L","A","N","S","A","P"],
		["O","O","G","O","T","P","N"],
		["H","P","O","L","A","N","O"]]
word = "POLAND"
print(exist(board, word))