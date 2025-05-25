# Last updated: 25/05/2025, 21:12:44
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        lis=ListNode()
        cur=lis
        i=0
        carry=0
        while(1):
            temp_sum=0
            if l1!=None and l2!=None:
                m=l1.val
                n=l2.val
                temp_sum=m+n+carry
                carry=(temp_sum-(temp_sum%10))/10
                temp_sum=temp_sum%10
                l1=l1.next
                l2=l2.next
            elif l1==None and l2!=None:
                n=l2.val
                temp_sum=n+carry
                carry=(temp_sum-(temp_sum%10))/10
                temp_sum=temp_sum%10
                l2=l2.next
            elif l2==None and l1!=None:
                m=l1.val
                temp_sum=m+carry
                carry=(temp_sum-(temp_sum%10))/10
                temp_sum=temp_sum%10
                l1=l1.next
            else:
                if carry!=0:
                    temp_sum=carry
                    cur.next=ListNode()
                    cur.next.val=temp_sum
                return lis
            cur.val=temp_sum
            if(l1 or l2):
                cur.next=ListNode()
                cur=cur.next
        return lis


        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        