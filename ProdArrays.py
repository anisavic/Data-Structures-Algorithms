class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # output = [1] * len(nums)
        # for index, num in enumerate(nums):
        #     orig_num = output[index]
        #     output = [num * o for o in output]
        #     output[index] = orig_num
        #     output[index] = int(output[index])
        # return output
        # Optimized solution: use prefixing, do two passes, once forward and another backward.. Product 
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        suffix = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        return [p * s for p, s in zip(prefix, suffix)]


if __name__ == "__main__":
    s = Solution()
    nums=[-1,0,1,2,3]
    # nums = [1, 2, 4, 6]
    print(s.productExceptSelf(nums))    
        