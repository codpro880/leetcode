class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        max_num = max(nums)
        set_nums = set(nums)
        for i in range(min_num, max_num):
            if i not in set_nums:
                return i
            
if __name__ == "__main__":
    sol = Solution()
    test = [3,2,9,8,0,1,4,5,7]
    print(sol.missingNumber(test))
