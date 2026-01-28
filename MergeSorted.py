class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #Merge Algorithm Test
        #for i in range(n+m):
        #    print(nums1[i])

        #create temp arrays
        L = [0] * m
        R = [0] * n


        for i in range(m):
            L[i] = nums1[i]
        for i in range(n):
            R[i] = nums2[i]

        i = 0
        j = 0
        k = 0

        while i < m and j < n:
            if L[i] < R[j]:
                nums1[k] = L[i]
                i += 1
            else:
                nums1[k] = R[j]
                j += 1
            k += 1

        while i < m:
            nums1[k] = L[i]
            i += 1
            k += 1

        while j < n:
            nums1[k] = R[j]
            j += 1
            k += 1

        return nums1
    def __init__(self): #test
        arr1 = [1, 2, 3, 0, 0, 0]
        arr2 = [2, 5, 6]
        print(self.merge(arr1, 3, arr2, 3))

def main():
    example = Solution()

if __name__ == "__main__":
    main()
