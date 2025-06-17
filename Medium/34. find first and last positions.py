class Solution:
    def searchRange(self, array, target):
        left = self.binarySearch(array, target, True)
        right = self.binarySearch(array, target ,False)
        return [left, right]

    def binarySearch(self, array, target, isleft ):
        left = 0
        right = len(array)-1
        i = -1
        while left <= right:
            mid = (left+right)//2
            if target < array[mid]:
                right = mid -1
            elif target > array[mid]:
                left = mid + 1
            else:
                i = mid
                if isleft:
                    right = mid-1
                else:
                    left = mid + 1
        return i
    

if __name__ == "__main__":
    s1 = Solution()
    array = [5,7,7,8,8,10]
    target = 8
    print(s1.searchRange(array, target))


        
    