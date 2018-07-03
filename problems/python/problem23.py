"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_listnode(li):
    if not li:
        return
    print(li.val)
    print_listnode(li.next)

import bisect
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heads = sorted([listnode for listnode in lists], key=lambda listnode: listnode.val)

        remaining_list = [listnode.next for listnode in heads if listnode is not None]
        remaining_list = sorted(remaining_list, key=lambda listnode: listnode.val)

        result = ListNode(-999)
        cur = result
        
        while heads:
            # Now add one elt from remaining_list to heads
            cur.next = heads[0]
            heads = heads[1:] # Pop from front.
            cur = cur.next

            if len(remaining_list) > 0:
                next_elt = remaining_list[0]
                remaining_list = remaining_list[1:]
                remaining_list = self.insert_into_list(remaining_list, next_elt.next)
                heads = self.insert_into_list(heads, next_elt)

        return self.listify(result.next) # Added a dumby node to the front, so return the next one.

    def insert_into_list(self, li, listnode):
        """ Insert the listnode into the sorted (descending) li """
        if listnode is None:
            return li
        index_to_ins = bisect.bisect([node.val for node in li], listnode.val)
        result = li[:index_to_ins] + [listnode] + li[index_to_ins:]
        return result

    def listify(self, listnode):
        cur = listnode
        result = [cur.val]
        while cur.next:
            result.append(cur.next.val)
            cur = cur.next
        return result

if __name__ == "__main__":
    sol = Solution()

    x = ListNode(1)
    x.next = ListNode(4)
    x.next.next = ListNode(5)

    y = ListNode(1)
    y.next = ListNode(3)
    y.next.next = ListNode(4)

    z = ListNode(2)
    z.next = ListNode(6)

    li = [x, y, z]
    
    result = sol.mergeKLists(li)
    #print_listnode(result)
    print(result)
