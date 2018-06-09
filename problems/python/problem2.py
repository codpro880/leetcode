"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pass

if __name__ == "__main__":
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

    # Node 1 setup
    l1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    l1.next = node2
    node2.next = node3

    # Node 2 setup
    l2 = ListNode(5)
    node4 = ListNode(6)
    node5 = ListNode(4)
    l2.next = node4
    node4.next = node5
    print(l1.val)
    print(l1.next.val)
    print(l1.next.next.val)
    #print("Should be 7 -> 0 -> 8", addTwoNumbers(
