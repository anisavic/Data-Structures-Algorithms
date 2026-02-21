class Solution:
    """
    example with index 7-1=6, and minimum is 6, so 6*6=36
    find maximum amount of water
    two-pointer solution. Maybe keep track of max's?
    We want bars to be high and to be as wide as possible.
    maybe hold max from both ends, if there is a larger one, but it will be narrower, so check if it is better volume than previous
    4 options to compare from?
    start with left and right
    move towards each other until left crosses right
    keep track of bestleft and best right
    once we move left and right by 1, either old solution is still best,
    or left better and right same
    or left same and right better
    or left better and right better
    update by checking which has highest volume and set the new left/right
    at the end, return maxwater

    # set bestleft to 0, bestright to the end
    maxwater initialized with form.
    for left in range(heights)
    right = heigts[length - left - 1]

    New solution, think about the heights, with each step, you want to encounter a taller pole

    """
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best_left = left #best bar on left
        best_right = right # best on right
        max_water = (best_right - best_left) * min(heights[best_left], heights[best_right])

        while left < right:
            #calc area
            water = (right - left) * min(heights[left], heights[right])
            #check if area improved
            if water > max_water:
                max_water = water

            #Make strategic descision, move bar that is minimum
            if min(heights[left], heights[right]) == heights[left]:
                left += 1
            else:
                right -= 1
            
        return max_water