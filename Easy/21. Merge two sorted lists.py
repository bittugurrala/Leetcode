
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode("dummy")
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next

# Time Complexity: O(n + m) where n and m are the lengths of list1 and list2 respectively.
# Space Complexity: O(1) since we are using a constant amount of extra space for the dummy node and tail pointer.
# The algorithm iterates through both lists, comparing their values and linking them in sorted order.

#The input is given as two linked lists, and the output is a single linked list that contains all the elements from both input lists in sorted order.
# The function uses a dummy node to simplify the merging process and a tail pointer to keep track of the last node in the merged list.
# The while loop continues until one of the lists is fully traversed, at which point the remaining elements from the other list are appended to the merged list.
# The final merged list is returned starting from the node after the dummy node.
