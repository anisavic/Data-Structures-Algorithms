class Solution:
    def numOfWays(self, n: int) -> int:
        """
        nx3 grid
        x x x (n=1) 3 x 2 x 2 = total #

        x x x
        x x x (n=2) 3 x 2*2

        Note, only 2 possibilities for column: either 2 same 1 diff, or all 3 diff
        ABA or ABC
        Base Case:
        ABA : 3x2x1 = 6 possibilities
        ABC : 3x2x1 = 6 possibilities
        total = 12

        now add another column: aba|abc x they cant be side by side
        aa
        bb
        ac X no, if you want aba with abc, you are reduced to 2x1x1=2
        aba with aba 3 ways=3

        aa
        bb
        cc abc with abc, 2 x 1 x 1=2
        abc with aba 2

        recurrence aba_n # ways to paint given nth is aba
        abc_n # ways to paint given nth is abc

        aba_n+1 = 3*aba_n + 2*abc_n
        abc_n+1 = 2*aba_n + 2*abc_n

        base:
        aba_1 = 6 # hold arrays for them
        abc_1 = 6

        from i = 2 to n:
        do the recurrence
        i = i-1...

        finally, return sum of both at n

        """
        MOD = (10**9 + 7)

        aba = 6 # ways to color given ith is aba
        abc = 6 # ways to color given ith is abc


        for i in range(2, (n+1)):
            new_aba = 3 * aba + 2 * abc
            new_abc = 2 * aba + 2 * abc

            aba, abc = new_aba, new_abc
        
        num_colorings = (aba + abc) % MOD
        
        return num_colorings