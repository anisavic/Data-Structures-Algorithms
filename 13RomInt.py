class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Hash Roman to Int pair
        Symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        current = 0 #starting indices
        next = 1
        res = 0

        #edge: if only 1 char:
        if len(s) == 1:
            return Symbol[s]

        while next < len(s):
            currChar = s[current]
            nextChar = s[next]
            if Symbol[currChar] >= Symbol[nextChar]:
                res += Symbol[currChar]
                current = next
                next += 1
            else: # else, current is smaller than next, subtract
                res += Symbol[nextChar] - Symbol[currChar]
                current += 2
                next += 2

        if current < len(s):
            res += Symbol[s[current]]

        return res




def main():
    s = Solution()
    print(s.romanToInt("MCMXCIV"))

if __name__ == '__main__':
    main()
