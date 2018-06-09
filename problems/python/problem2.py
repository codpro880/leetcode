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
        l1_num = self.get_as_number(l1)
        l2_num = self.get_as_number(l2)
        result_num = l1_num + l2_num
        return self.make_list_node(result_num)

    def get_as_number(self, li):
        """ Takes a list node, returns the int it represnts """
        digit_list = [li.val]
        cur = li.next
        while True:
            if cur is None:
                break
            else:
                digit_list.append(cur.val)
                cur = cur.next
                
        digit_list_str = [str(x) for x in digit_list]
        return int("".join(digit_list_str[::-1]))

    def make_list_node(self, num):
        result = []
        num_as_str = str(num)
        for char in num_as_str[::-1]:
            result.append(int(char))

        result_list_node = ListNode(result[0])
        cur = result_list_node
        for digit in result[1:]:
            cur.next = ListNode(digit)
            cur = cur.next

        return result_list_node

def print_listnode(li):
    cur_node = li
    print("PRINTING!")
    while True:
        if cur_node is not None:
            print("cur_node.val: " + str(cur_node.val))
            cur_node = cur_node.next
        else:
            print("Returned...")
            return

if __name__ == "__main__":
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

    # Node 1 setup
    l1 = ListNode(1)
    node2 = ListNode(8)
    node3 = ListNode(3)
    l1.next = node2
    node2.next = node3
    print(l1.val)
    print(l1.next.val)
    print(l1.next.next.val)

    # Node 2 setup
    l2 = ListNode(7)
    node4 = ListNode(1)
    l2.next = node4
    print(l2.val)
    print(l2.next.val)
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print("Should be 8 -> 9 -> 3")
    print_listnode(result)
