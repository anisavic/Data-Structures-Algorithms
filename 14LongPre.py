class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        #find longest string
        longest = max(strs, key=len)

        prefix = ""

        for charIndex in range(len(longest)):
            for str in strs:
                try:
                    index = str[charIndex]
                    if str[charIndex] != longest[charIndex]:
                        return prefix
                except IndexError:
                    return prefix

            prefix += longest[charIndex]

        return prefix



def main():
    s = Solution()
    print(s.longestCommonPrefix(["", "b"]))
    strexample = "hello world"
    #print(strexample[1000])
    try:
        print(strexample[1000])
    except IndexError:
        print("index out of Range")

if __name__ == '__main__':
    main()