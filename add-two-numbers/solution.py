# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 2 4 3->3 4 2
        # 5 6 4->4 6 5
        #     8 0 7->7 0 8
        num1="" #243
        num2="" #564
        while l1!=None:
            num1=num1+str(l1.val)
            l1=l1.next
        while l2!=None:
            num2=num2+str(l2.val)
            l2=l2.next
        num1=num1[::-1]
        num2=num2[::-1]
        res=int(num1)+int(num2) #807
        res=str(res)[::-1]#708

        head=ListNode(int(res[0])) #7 -> None
        current=head #7->None 
        for i in res[1:]:#708
            current.next=ListNode(int(i)) #0->None
            current=current.next #8->None
        return head
        