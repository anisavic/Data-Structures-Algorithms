class Solution:
    """
    can we find the minimum element of list given we know it is 
    rotated in logn time??
    basically, we can binary search, to find the rotating point or 
    rotated point, since that is where it is the minimum value
    3,4,5,6,1,2
    check the middle
    mid is 2(5)
    5 is greater than 2, search right by updating left and right
    left = 3, right stays right
    update mid regardless

    iterate, binary search style
    5,6,7,8,9,10,1,2,3,4
    5 to 10/2=5 (10) higher
    10 to 5 + 10/4=5+2=7(2) lower
    2 to 7 - 10/8=6(1) lower
    1 to 6 - 10/16(DONE!)

    Basically, do a while loop until we cant go down anymore
    going up if we see higher numbers
    going down if we see lower numbers
    have a current_element, start with first element
    then go to top half while fraction of size/step is greater than 0 (int)
    compute next index based on if higher, go up if lower go back

    result will be the minimum

    current_element = first element
    next_index = 0 + n/step
    step = 2 #start with it and keep compoubnding

    while size/step is greater than 0
        if value at next is greater than current
        increment next index
        if less than current
        decrement next
        
        either way update current to value at next

    problem: 4,5,6,7 returns 7
    4 to 6 higher
    6 to 7 higher
    done

    problem: 2,3,1:

    Ditch the pointer search, and do real binary search with
    a left and right pointer
    left =0 
    right = len-1
    mid = (left + right) // 2
    while left < right:
        if mid greater than right
        increment and update left to hold +1 index of mid, keep right sam
        if right greater than mid
        must be somewhere in left, update right to be mid

        update mid regardless
    
    return mid



    """
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while left < right:
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            mid = (left + right) // 2

        return nums[mid]




        

if __name__ == "__main__":
    t = Solution()
    test = [3,4,5,6,1,2]
    print(t.findMin(test))