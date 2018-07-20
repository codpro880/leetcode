class Solution:
    def hammingDistance(self, x, y):
        bits_x = str(bin(x)[2:])
        bits_y = str(bin(y)[2:])
        bits_x, bits_y = self.pad_to_equal_len(bits_x, bits_y)
        num_bits_diff = self.xor(bits_x,  bits_y)
        return num_bits_diff

    def pad_to_equal_len(self, bits_x, bits_y):
        if len(bits_x) < len(bits_y):
            num_zeros = len(bits_y) - len(bits_x)
            bits_x = "0"*num_zeros + bits_x
        else:
            num_zeros = len(bits_x) - len(bits_y)
            bits_y = "0"*num_zeros + bits_y

        return bits_x, bits_y

    def xor(self, bits_x, bits_y):
        result = 0
        for bx, by in zip(bits_x, bits_y):
            if bx != by:
                result += 1
        return result

if __name__ == "__main__":
    sol = Solution()
    x = 1
    y = 4
    result = sol.hammingDistance(x, y)
    print(result)
