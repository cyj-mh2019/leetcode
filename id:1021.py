class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = 0
        mem = ''
        output = ''
        for sym in S:
            if sym=='(':
                stack = stack + 1
            else:
                stack = stack - 1
            if stack == 0:
                output = output + mem[1:]
                mem = ''
            else:
                mem = mem + sym
        return output
#简单的栈应用括号匹配 将output和mem换成list会更快 可能是str的处理比list慢
