class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #first, find the unique elements
        uniqueElem = []
        for elem in nums: #find unique elements
            if elem not in uniqueElem:
                uniqueElem.append(elem)

        #print(f'Unique elements are: {uniqueElem}')

        #Count up number of repetitions for each unique element
        numReps = [0] * len(uniqueElem)
        #print(numReps)
        for elem in nums:
            index = uniqueElem.index(elem)
            numReps[index] += 1
        #print(numReps)

        #maximum value is at index with maximum repetitions
        maxIndex = numReps.index(max(numReps))
        #print(maxIndex)
        return uniqueElem[maxIndex]

# '''
#         ###MORE EFFICIENT SOLUTION: CHATGPT TOLD ME THIS ONE:
#         count = 0
#         candidate = None
#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)
#         return candidate
# '''
def main():
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))
    print(s.majorityElement([3,2,3]))

if __name__ == '__main__':
    main()
