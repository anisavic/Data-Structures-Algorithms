class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        smappings = {}
        tmappings = {}
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            try:
                if smappings[sChar] != tChar:
                    return False
            except KeyError:
                smappings[sChar] = tChar
            try:
                if tmappings[tChar] != sChar:
                    return False
            except KeyError:
                tmappings[tChar] = sChar
        return True

def main():
    s = Solution()
    print(s.isIsomorphic("paper", "title"))


if __name__ == '__main__':
    main()



