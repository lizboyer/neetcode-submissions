# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode(None)
        list3_head = list3
        while list1 != None or list2 != None:
            # print("1 v 2:", list1.val, list2.val)
            if list1 == None and list2 != None: # list1 is empty, but list 2 is not
                print("list2")
                list3.next = list2 # add that node to list3
                list2 = list2.next # move list1 forward
            elif list2 == None and list1 != None: # list2 is empty, but list 1 is not
                print("list1")
                list3.next = list1 # add that node to list3
                list1 = list1.next # move list1 forward
            elif list1.val <= list2.val: # if list1.val is smaller
                print("list1")
                list3.next = list1 # add that node to list3
                list1 = list1.next # move list1 forward
            elif list1.val > list2.val: # if list2.val is smaller
                print("list2")
                list3.next = list2 # add that node to list3
                list2 = list2.next # move list1 forward
            list3 = list3.next
            print("list3 curr, next:", list3.val)

        return list3_head.next