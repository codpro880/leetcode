import numpy as np
class Solution:
    def spiralOrder(self, matrix):
        return self.spiral_order_helper(matrix, [])

    def spiral_order_helper(self, matrix, res):
        matrix = np.array(matrix)
        if matrix.size == 0:
            return res
        if 1 in matrix.shape:
            new_res = list(matrix.flatten())
            return self.spiral_order_helper(matrix[1:-1, 1:-1], res + new_res)            
        try:
            len(matrix[0])
            new_res = list(matrix[0, :]) + list(matrix[:, -1][1:]) + list(matrix[-1, :][:-1][::-1]) + list(matrix[:, 0][1:-1])
        except:
            new_res = list(matrix)
        return self.spiral_order_helper(matrix[1:-1, 1:-1], res + new_res)

if __name__ == "__main__":
    sol = Solution()
    x = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
        ]
    #print(sol.spiralOrder(x))

    x = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
        ]

    print(sol.spiralOrder(x))
