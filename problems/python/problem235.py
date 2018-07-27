# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestor_map = self.create_ancestor_map(root)
        p_map = ancestor_map[p]
        q_map = ancestor_map[q]
        for ancestor in p_map:
            if ancestor in q_map:
                return ancestor
            
    def create_ancestor_map(self, root):
        my_map = {}
        self.create_ancestor_map_h(root, my_map)
        return my_map
        
    def create_ancestor_map_h(self, root, my_map):
        if root is None:
            return my_map
        if root.val not in my_map:
            my_map[root.val] = [root.val]
        if root.left:
            my_map[root.left.val] = [root.left.val] + my_map[root.val]
            self.create_ancestor_map_h(root.left, my_map)
        if root.right:
            my_map[root.right.val] = [root.right.val] + my_map[root.val]
            self.create_ancestor_map_h(root.right, my_map)
            
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
    
    sol = Solution()

    print(sol.lowestCommonAncestor(four, 1, 3))
    print(sol.lowestCommonAncestor(four, 4, 7))
