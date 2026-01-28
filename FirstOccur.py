class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1



def main():
    haystack = "sadbutsad"
    needle = "sad"
    s = Solution()
    print(s.strStr(haystack, needle))\

if __name__ == '__main__':
    main()