import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        len_of_str = len(string)
        num_iterations = int(len_of_str / 2) # Only go through half the list

        for i in range(num_iterations):
            if string[i] != string[-1 - i]:
                return False
            
        return True


if __name__ == '__main__':
    sol = Solution()
    palindrome = " "
    print(f"Function Return: {sol.isPalindrome(palindrome)}")

