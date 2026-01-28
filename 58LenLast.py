class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #s = s.strip() #strip of trailing

        arr = s.split()
        last = arr[len(arr)-1]
        return len(last)

def main():
    s = Solution()
    print(s.lengthOfLastWord("joyboy"))

if __name__ == '__main__':
    main()

