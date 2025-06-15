"""
Problem: https://leetcode.com/problems/sort-an-array/description/?envType=problem-list-v2&envId=merge-sort
LC 1859. Sort an array
Difficulty: Medium
Approach: Using recursions O(nlog(n))"""

class Solution:
    def sortArray(self, array: List[int]) -> List[int]:
        mid = len(array)//2
        if len(array) == 1:
            return array
        array1 = self.sortArray(array[: mid])
        array2 = self.sortArray(array[mid: ])
        return self.conquer(array1, array2)
        

    def conquer (self, array1, array2):
        m , n = 0,0
        res = []
        while m < len(array1) and n <len(array2):
            if array1[m] < array2[n]:
                res.append(array1[m])
                m = m+ 1
            else:
                res.append(array2[n])
                n = n + 1
        
        res.extend(array1[m: ])
        res.extend(array2[n: ])

        return res




#Time complexity: O(nlog(n)

#Using merge sort for sorting involvign recurrsion is the bext approch for sorting the array. 
