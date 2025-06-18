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


        
"""
This is a new varaition of Binary search that, it has more than finding the target in the array 

there are many other variations of this; 

|                Goal                 |                      Modification                                             |                      
| ------------------------------------| ----------------------------------------------------------------------------- |
| Find "first occurrence" of target   | Keep searching left even after match (`right = mid-1`)                        |
| Find "last occurrence" of target    | Keep searching right after match (`left = mid+1`)                             |
| Find "insert position" of target    | Store `mid` and update bounds based on `target < arr[mid]`                    |
| Search in "rotated array"           | Add logic to check which side is sorted                                       |
| Find "minimum" in rotated array     | No need to match `target`, just shrink toward min                             |
| First element "greater/less than k" | Adjust conditions like `if arr[mid] <= k: left = mid + 1`                     |
| Infinite array                      | Exponentially increase bounds until `arr[right] > target`, then binary search |
| 2D Matrix search                    | Treat 2D as 1D (`mid = (left + right)//2`, then row/col math)                 |

in a nutshell, the important this we have to notice is, 
thinking about the situations we have make changes to the Tradinational binary search.

Gerenarally we have these situations; 

s01. We need bounds or ranges, not just existence

s02. The array has duplicates

s03. The array is rotated

s04. The array is infinite or virtual (like index function)

s05. The condition is not direct equality

where to find these? here are few questoins that falls under this category; 

LC 33
LC 34
LC 35
LC 162
LC 153



"""