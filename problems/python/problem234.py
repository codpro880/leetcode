"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Just make a stack and use fast/slow pointer trick.
# Step fast by 2, slow by 1, when fast at end, slow will be in middle.
# Create stack of values from slow as we step
# Now just keep going with slow (in middle), and pop from stack as we go


class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        runner_slow = head
        runner_fast = head
        vals = []

        while runner_fast:
            vals.append(runner_slow.val)
            if runner_fast.next:
                runner_fast = runner_fast.next.next
            else:
                break
            runner_slow= runner_slow.next

            runner_fast = head

        while runner_slow:
            if vals.pop() != runner_slow.val:
                return False
            runner_slow = runner_slow.next

        return len(vals) == 0
