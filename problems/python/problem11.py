"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
# This problem statement isn't clear...expected to return just one value (max area), not two?
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        num_nonzero = len([h for h in height if h > 0])
        if num_nonzero <= 1:
            return 0

        best_area = 0
        first_ind = 0
        last_ind = len(height) - 1
        while (first_ind < last_ind):
            print("First ind: ", first_ind)
            print("last ind: ", last_ind)
            cur_area = min(height[first_ind], height[last_ind]) * (last_ind - first_ind)
            if cur_area > best_area:
                best_area = cur_area
            
            if height[first_ind] < height[last_ind]:
                first_ind += 1
            else:
                last_ind -= 1

        return best_area


if __name__ == "__main__":
    sol = Solution()
    print("Result 15000: ", sol.maxArea(height=range(15000)))
    print("Should be 1: ", sol.maxArea([1,1]))
