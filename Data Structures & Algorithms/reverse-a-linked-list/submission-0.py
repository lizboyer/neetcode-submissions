# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while(head):
            prev_head = head # save the last head
            head = head.next # iterate through linked list
            prev_head.next = prev # set prev head next to preev head
            
            # print(prev_head.val, prev_head.next.val)
            prev = prev_head
            # print("prev val, next val:", prev_head.val, prev_head.next.val)
        head = prev
        return head