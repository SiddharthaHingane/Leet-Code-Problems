# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        trav = head
        size = 0
        while True:
            size += 1
            trav = trav.next
            if trav == None:
                break
        
        if size == 1:
            return None
        
        if size == n:
            return head.next
        
        
        trav = head
        while size != n + 1:# or you can write size - n - 1 != 0 :
            trav = trav.next
            n+=1
        
        trav.next = trav.next.next
        return head
