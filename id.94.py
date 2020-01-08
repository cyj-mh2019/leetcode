class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res
'''
 颜色标记法，可以统一 先序，中序，后序的栈遍历.只需改变入栈顺序即可
* 访问过的节点         标记灰色
* 未访问过的节点       标记白色
* 遇到白色节点 按遍历顺序将左中右节点依次入栈
* 遇到灰色节点 输出节点值

'''

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        travel_list = []
        stack = []
        p = root
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            travel_list.append(p.val)
            p = p.right
        return travel_list  
