class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s.replace() and s.lower
        # Format str first into all lower and no spaces
        # s = s.lower()
        # s = s.replace(" ", "")
        # alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
        # 'q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'}
        # for c in s:
        #     if c not in alpha:
        #         s = s.replace(c, "", 1)
        # s = "".join(c.lower() for c in s if c.isalnum()) # Better using join
        
        # for i in range(int(len(s)/2)):
        #     if s[i] != s[-1 - i]:
        #         return False
        # return True # This is an okay solution, but still O(n) space... We could eliminate the need to store the cleaned str entirely
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True
    

if __name__ == "__main__":
    s = Solution()
    str=".,"
    print(s.isPalindrome(str))
