class Node(object):
    def __init__(self, val):
        self.val = val
        self.adj = []
        self.visited = False

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Turn str into nodes
        if not word:
            return True
        if not board:
            return False
        
        nodes = self.build_nodes(board)
        return self.has_word(nodes, word)
    
    def has_word(self, nodes, word):
        first_char = word[0]
        for row in nodes:
            for node in row:
                if node.val == first_char:
                    # Do DFS to see if we can link the rest of the chars
                    self.reset_visited(nodes)
                    return self.search(node, word)
                
    def reset_visited(self, nodes):
        for row in nodes:
            for node in row:
                node.visited = False
    
    def search(self, node, word):
        if not word:
            return True
        if node.visited:
            return False
        node.visited = True
        
        if node.val == word[0]:
            result = []
            for adj_node in node.adj:
                result.append(self.search(adj_node, word[1:]))
            return any(result)
        else:
            return False
            
    def build_nodes(self, board):
        nodes = []
        for i in range(len(board)):
            nodes.append([])
            for j in range(len(board[0])):
                node = Node(board[i][j])
                nodes[i].append(node)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                adj = self.get_adj(nodes, i, j)
                nodes[i][j].adj = adj
                
        return nodes
    
    def get_adj(self, nodes, i, j):
        adj = []
        try: # up
            if i-1 >= 0:
                adj.append(nodes[i-1][j])
        except IndexError:
            pass
        try: # down
            adj.append(nodes[i+1][j])
        except IndexError:
            pass
        try: # left
            if j-1 >= 0:
                adj.append(nodes[i][j-1])
        except IndexError:
            pass
        try: # right
            adj.append(nodes[i][j+1])
        except IndexError:
            pass
        return adj
    
if __name__ == "__main__":
    sol = Solution()
    board = [["a", "b", "c", "d"],
             ["e", "f", "g", "h"],
             ["i", "j", "k", "l"]]
    word = "abcd"
    print("True: ", sol.exist(board, word))
    
