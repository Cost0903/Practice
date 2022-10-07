# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # think: we need to move the head and slow, the head will twice faster then slow, make sure the slow will the middle value
        slow = head
        while head and head.next: # we need to stop when the head and head.next is null
            slow = slow.next # normal speed to make sure it will stop at middle value
            head = head.next.next # twice speed
            # head = [1,2,3,4] > move to 3 > move to 4  
            # slow = head      > move tp 2 > move to 3
        return slow

# Time Complexity :  O(n)   while head = n
# Space Complexity : O(1)
