class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        self.num_to_word_map = self.gen_num_to_word_map()
        return self.num_to_word_h(num)

    def num_to_word_h(self, num):
        # Get place first
        if num in self.num_to_word_map:
            return self.num_to_word_map[num]
        if num <= 99:
            tens_place = int(str(num)[0])
            rest = int(str(num)[1:])
            return self.num_to_word_map[tens_place*10] + " " + self.num_to_word_h(rest)
        elif num <= 999:
            hundreds_place = int(str(num)[0])
            rest = int(str(num)[1:])
            return self.num_to_word_map[hundreds_place] + " Hundred " + self.num_to_word_h(rest)
        elif num <= 999999:
            if len(str(num)) == 4:
                slice_stop = 1
            elif len(str(num)) == 5:
                slice_stop = 2
            else:
                slice_stop = 3
            thousands_place = int(str(num)[:slice_stop])
            rest = int(str(num)[slice_stop:])
            return self.num_to_word_h(thousands_place) + " Thousand " + self.num_to_word_h(rest)
        elif num <= 999999999:
            if len(str(num)) == 7:
                slice_stop = 1
            elif len(str(num)) == 8:
                slice_stop = 2
            else:
                slice_stop = 3
            thousands_place = int(str(num)[:slice_stop])
            rest = int(str(num)[slice_stop:])
            return self.num_to_word_h(thousands_place) + " Million " + self.num_to_word_h(rest)
        elif num <= 999999999999:
            if len(str(num)) == 10:
                slice_stop = 1
            elif len(str(num)) == 11:
                slice_stop = 2
            else:
                slice_stop = 3
            thousands_place = int(str(num)[:slice_stop])
            rest = int(str(num)[slice_stop:])
            return self.num_to_word_h(thousands_place) + " Billion " + self.num_to_word_h(rest)

    def gen_num_to_word_map(self):
        num_to_word = {}
        num_to_word[0] = ""
        num_to_word[1] = "One"
        num_to_word[2] = "Two"
        num_to_word[3] = "Three"
        num_to_word[4] = "Four"
        num_to_word[5] = "Five"
        num_to_word[6] = "Six"
        num_to_word[7] = "Seven"
        num_to_word[8] = "Eight"
        num_to_word[9] = "Nine"
        num_to_word[10] = "Ten"
        num_to_word[11] = "Eleven"
        num_to_word[12] = "Twelve"
        num_to_word[13] = "Thirteen"
        num_to_word[14] = "Fourteen"
        num_to_word[15] = "Fifteen"
        num_to_word[16] = "Sixteen"
        num_to_word[17] = "Seventeen"
        num_to_word[18] = "Eightteen"
        num_to_word[19] = "Nineteen"
        num_to_word[20] = "Twenty"
        num_to_word[30] = "Thirty"
        num_to_word[40] = "Fourty"
        num_to_word[50] = "Fifty"
        num_to_word[60] = "Sixty"
        num_to_word[70] = "Seventy"
        num_to_word[80] = "Eighty"
        num_to_word[90] = "Ninety"
        return num_to_word

if __name__ == "__main__":
    sol = Solution()
    num = 555
    print("555: ", sol.numberToWords(555))

    print("123456:", sol.numberToWords(123456))
    print("12345678:", sol.numberToWords(12345678))
    print("12345678910:", sol.numberToWords(12345678910))
    print("1000:", sol.numberToWords(1000))
