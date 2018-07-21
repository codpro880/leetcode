"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        cur = head
        result = ListNode(head.val)
        result.next = None
        cur = cur.next

        while cur:
            temp = cur.next
            cur.next = result
            result = cur
            cur = temp

        return result

    def printListNode(self, ln):
        cur = ln
        while cur:
            print(cur.val)
            cur = cur.next


class SolutionRecursive(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        else:
            return self.rev_list_helper(head, None)

    def rev_list_helper(self, head, prev):
        if head is None:
            return head
        else:
            if head.next is None:
                head.next = prev
                return head

            single_head = ListNode(head.val)
            single_head.next = prev
            rest = self.rev_list_helper(head.next, single_head)
                
            return rest
        

    def printListNode(self, ln):
        cur = ln
        while cur:
            print(cur.val)
            cur = cur.next

if __name__ == "__main__":
    sol = SolutionRecursive()

    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    one.next = two
    two.next = three
    three.next = four
    four.next = five

    sol.printListNode(one)

    result = sol.reverseList(one)
    print("REV")

    sol.printListNode(result)
    
