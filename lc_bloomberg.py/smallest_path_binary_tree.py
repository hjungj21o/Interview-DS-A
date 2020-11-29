def smallestpath(root):
    if not root:
        return ""

    smallest_str = "z"

    def dfs(node, curr_str=""):
        nonlocal smallest_str
        curr_str = node.val + curr_str
        print(curr_str)
        if not node.left and not node.right:
            cur_str_min = ord(curr_str[0])
            smallest_str_min = ord(smallest_str[0])
            print(smallest_str_min)
            smallest_str = smallest_str if smallest_str_min < cur_str_min else curr_str

        if node.left:
            dfs(node.left, curr_str)
        if node.right:
            dfs(node.right, curr_str)

    dfs(root)

    return smallest_str


class TreeNode:
    def __init__(self, val="", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


Aa = TreeNode("A")
E = TreeNode("E")
C = TreeNode("C")
D = TreeNode("D")
D.left = Aa
B = TreeNode("B")
B.left = D
B.right = E
A = TreeNode("A")
A.left = B
A.right = C

print(smallestpath(A))
