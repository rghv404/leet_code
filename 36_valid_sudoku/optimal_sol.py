class Solution:
    def isValidSudoku_orig(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # first we check for valid ints
        # for row in board:
        #     if any(len(item) > 1 or int(item) < 1 or int(item) > 9
        for item in row):
        #         return False
        empty = '.'
        # cheicng in col in n**2 time
        for col in zip(*board):
            dict_ = {}
            for item in col:
                if item in dict_ and item is not empty:
                    return False
                elif item is not empty:
                    dict_[item] = 1

        # checking in row in n**2 time
        for row in board:
            dict_ = {}
            for item in row:
                if item in dict_ and item is not empty:
                    return False
                elif item is not empty:
                    dict_[item] = 1

        # checking in 3*3 mini board in n**2 time
        for r in range(3):
            for c in range(3):
                dict_ = {}
                for i in range(3):
                    for j in range(3):
                        item = board[3*r + i][3*c + j]
                        if item in dict_ and item is not empty:
                            return False
                        else:
                            dict_[item] = 1
        return True

    def isValidSudoku(self, board):
        empty = '.'
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        mini_board_set = [set() for _ in range(9)]

        def board_set_index(i,j):
            i = i//3
            j = j//3
            return 3*i + j

        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item is not empty:
                    k = board_set_index(i, j)
                    if item in row_sets[i] or item in col_sets[j] or item in mini_board_set[k]:
                        return False
                    else:
                        row_sets[i].add(item)
                        col_sets[j].add(item)
                        mini_board_set[k].add(item)
        return True
