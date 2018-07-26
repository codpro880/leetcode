"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""
# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.gen = self.in_order(self.root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return True

    def next(self):
        """
        :rtype: int
        """
        return next(self.gen)

    def in_order(self, root):
        if root:
            if root.left:
                yield from self.in_order(root.left)
            yield root.val
            if root.right:
                yield from self.in_order(root.right)

if __name__ == "__main__":
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)

    four.left = two
    four.right = six
    two.left = one
    two.right = three
    six.left = five
    six.right = seven

    bsti = BSTIterator(four)
    for _ in range(7):
        print("NEXT: ", bsti.next())
