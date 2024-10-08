class Solution(object):
    def intToRoman(self, num):
        roman_numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_numeral_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for i in range(len(roman_numeral_values)):
            while num >= roman_numeral_values[i]:
                result += roman_numerals[i]
                num -= roman_numeral_values[i]
        return result

num = 3
s = Solution()
print(s.intToRoman(num))

