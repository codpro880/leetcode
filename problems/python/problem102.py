from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def level_traversal(root):
    if not root:
        return []
    queue = deque()
    root.level = 0
    queue.append(root)
    res = []
    while queue:
        cur = queue.popleft()
        try:
            res[cur.level].append(cur.val)
        except IndexError:
            res.append([])
            res[cur.level].append(cur.val)
        if cur.left:
            cur.left.level = cur.level + 1
            queue.append(cur.left)
        if cur.right:
            cur.right.level = cur.level + 1
            queue.append(cur.right)

    return res

if __name__ == "__main__":
    three = TreeNode(3)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seven = TreeNode(7)

    three.left = nine
    three.right = twenty

    twenty.left = fifteen
    twenty.right = seven

    result = level_traversal(three)
    print(result)
