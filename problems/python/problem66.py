class Solution(object):
    def plusOne(self, digits):
        num = int("".join([str(x) for x in digits])) + 1
        return [int(x) for x in str(num)]
