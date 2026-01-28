

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        charFrequencies = {chr(x): 0 for x in range(97, 123)}
        for char in ransomNote:
            charFrequencies[char] += 1

        #print(charFrequencies)
        for char in magazine:
            charFrequencies[char] -= 1

        if any(val >= 1 for val in charFrequencies.values()):
            return False
        else:
            return True


def main():
    s = Solution()
    print(s.canConstruct("aa", "aab"))


if __name__ == '__main__':
    main()

