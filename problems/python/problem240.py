import bisect
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or matrix == [[]]:
            return False
        first_col = [matrix[i][0] for i in range(len(matrix))]
        max_row_ind = bisect.bisect_right(first_col, target) - 1
        max_col_ind = bisect.bisect_right(matrix[0], target) - 1
        if matrix[max_row_ind][max_col_ind] == target:
            return True
        for row_ind in range(max_row_ind+1):
            target_ind = bisect.bisect_right(matrix[row_ind], target, hi=max_col_ind+1) - 1
            if matrix[row_ind][target_ind] == target:
                return True
        return False
                
            
if __name__ == "__main__":
    sol = Solution()
    m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
p  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
#     print("True: ", sol.searchMatrix(m, 5))
#     print("False: ", sol.searchMatrix(m, 20))

    m = [[-5]]
    #print(sol.searchMatrix(m, -5))
    
    m = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    print("True: ", sol.searchMatrix(m, 19))
