class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        """
        @return the next smallest number
        """
        root = self.stack.pop()
        node = root.right
        while node:
            self.stack.append(node)
            node = node.left
        return root.val

       

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
        
  #题目要求 next方法的时间复杂度为o(1),这个方法每一个节点都要使用一次 一共需要 n-1次（除了根节点）,结合初始化 实际上是一次完整的前序遍历 复杂度为o(n)
  所以单次的next的方法的复杂度为o(1) 这种分析方法称为 摊还分析 参考资料：<算法导论>-第17章-摊还分析。
