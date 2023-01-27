# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# # Solution 1
class Solution:
    def addTwoNumbers(self, l1, l2):
        root = ListNode(0)
        result = root
        carry = 0

        while l1 or l2 or carry:
            
            if l1:
                carry += l1.val
                l1 = l1.next
            
            if l2:
                carry += l2.val
                l2 = l2.next

            result.next = ListNode(carry%10)
            result = result.next
            carry = carry // 10

        return root.next

# # Solution 2
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         first_num, second_num = "", ""

#         while l1 != None:
#             first_num += str(l1.val)
#             l1 = l1.next

#         while l2 != None:
#             second_num += str(l2.val)
#             l2 = l2.next

#         summation = list(str(int(first_num) + int(second_num)))

#         digit_node = None

#         for index, value in enumerate(summation):

#             if index == 0:
#                 digit_node =  ListNode(val=value)
#                 continue

#             digit_node =  ListNode(val=value, next=digit_node)
        
#         return digit_node