class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sols = [0, 1, 2]

        for i in range(3, n + 1):
            sols.append(sols[i - 1] + sols[i - 2])

        return sols[n]

def main():
    s = Solution()
    print(s.climbStairs(3))

if __name__ == '__main__':
    main()