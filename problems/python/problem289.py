import itertools
class Solution(object):
    def gameOfLife(self, board):
        new_board = []
        for i in range(len(board)):
            row = []
            for j in range(len(board[i])):
                n_inds = itertools.product((i-1, i, i+1), (j-1, j, j+1))
                n_inds = [x for x in n_inds if x[0] >= 0 and x[0] <= len(board) - 1 and x[1] >= 0 and x[1] <= len(board[i]) - 1]
                n_inds = [x for x in n_inds if x != (i, j)] # remove self
                live = 0
                for n_ind in n_inds:
                    n = board[n_ind[0]][n_ind[1]]
                    if n == 1:
                        live += 1
                if board[i][j] == 1:
                    if live < 2:
                        row.append(0)
                    elif 2 <= live <= 3:
                        row.append(1)
                    else:
                        row.append(0)
                else:
                    if live == 3:
                        row.append(1)
                    else:
                        row.append(0)
            new_board.append(row)

        for i in range(len(new_board)):
            for j in range(len(new_board[i])):
                board[i][j] = new_board[i][j]

if __name__ == "__main__":
    sol = Solution()
    x = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
        ]
    sol.gameOfLife(x)
    print(x)
    
