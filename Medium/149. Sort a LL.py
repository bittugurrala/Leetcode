# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.divide(head)


    def middle(self, head):
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow 
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None
        return slow

    def divide(self, head):
        if not head or not head.next:
            return head
        mid = self.middle(head)
        left = self.divide(head)
        right = self.divide(mid)

        return self.conquer(left, right)

    def conquer(self, left, right):
        dummy = ListNode("dummy")
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next
        tail.next = left or right

        return dummy.next

"""

Time : O(nlog(n))
space : O(1)

The process is very simple as we sort an Array as to how we should have two different arrays, 
here we split the given Linkedlist into the two different linkedlists by finding the middle Node 

later we handle the splittrd linked lists as we using divine function

we sort by comparing each node of the lists usind concoqure function. 

later we create a method called as Merge_sort to call it as a function of the object. 
"""  