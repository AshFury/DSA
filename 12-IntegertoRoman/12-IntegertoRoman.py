# Last updated: 07/09/2025, 20:21:42
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]
        l2=[]
        if list1==None and list2==None:
            return list1
        while list1!=None:
            l1.append(list1.val)
            list1=list1.next
        while list2!=None:
            l2.append(list2.val)
            list2=list2.next
        l3=l1+l2
        l3.sort()
        new_lis=ListNode()
        res=new_lis
        for i in range(0,len(l3)):
            if i==len(l3)-1:
                new_lis.val=l3[i]
                return res
            new_lis.val=l3[i]
            new_lis.next=ListNode()
            new_lis=new_lis.next
        return res


        