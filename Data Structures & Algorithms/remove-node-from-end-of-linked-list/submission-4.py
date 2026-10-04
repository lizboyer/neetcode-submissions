# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        init_head = head
        return_head = head
        ctr = 0
        prev = None
        while(head):
            head = head.next
            ctr += 1
        for i in range(ctr-n):
            prev = init_head
            init_head = init_head.next
        if prev == None:
            return_head = return_head.next
        elif prev.next:
            prev.next = init_head.next
        else: return None
        return return_head