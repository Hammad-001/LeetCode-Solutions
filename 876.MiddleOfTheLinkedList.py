# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution 1


class Solution:

    def middleNode(self, head):
        Next = head
        Middle = head
        while Next and Next.next:
            Middle = Middle.next
            Next = Next.next.next
        return Middle

# Solution 2


class Solution:

    def middleNode(self, head):
        length = 1
        Next = head.next
        Middle = head

        while Next != None:

            if length % 2 == 0:
                Middle = Middle.next

            length += 1
            Next = Next.next

        if length % 2 == 0:
            return Middle.next

        return Middle
