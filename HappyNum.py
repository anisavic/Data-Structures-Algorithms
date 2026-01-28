class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''CHAT SOLUTION'''
        if n == 1:
            return True

        def get_next(num):
            return sum(int(digit) ** 2 for digit in str(num))

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        if slow == fast:
            return False
        else:
            return True


        ''''''
        '''MY SOLUTION
        #by hint that 31 bits are used, that's about 2 billion, so simply if that was 81*10=810
        sums = {x: (False) for x in range(1, 810)}
        currVal = self.compute_sum(n)
        while currVal != 1:
            if sums[currVal] == True:
                return False
            sums[currVal] = True
            currVal = self.compute_sum(currVal)
        return True
        '''


    def compute_sum(self, num):
        sum = 0
        val = num % 10
        vals = []
        while num != 0:
            vals.append(val)
            num //= 10
            val = num % 10


        for val in vals:
            sum += val**2
        return sum

def main():
    s = Solution()
    print(s.compute_sum(82))
    val = 2
    print('niggay')
    print(f'Is {val} happy? Answer is: ', s.isHappy(val))
    print(2**2 + 1**2 + 4 **2 + 7**2 + 4**2 + 8**2 + 3**2 + 6**2 + 4**2 + 7**2)
    print(9**2 + 9**2 + 9**2 + 9**2 + 9**2 + 9**2 + 9**2 + 9**2 + 9**2 + 0)


if __name__ == '__main__':
    main()
