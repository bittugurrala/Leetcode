class Solution:
    def searchInsert(self, array: List[int], target: int) -> int:
        left = 0
        right = len(array)-1
        index = -1
        while left <= right:
            mid = (left + right)//2
            if target > array[mid]:
                left = mid + 1
            elif target < array[mid]:
                right = mid -1
            else:
                return mid
        return left


# Time Complexity: O(log n)# Space Complexity: O(1)
# The time complexity is O(log n) because we are using binary search,
# which divides the search space in half with each iteration.              


        

        