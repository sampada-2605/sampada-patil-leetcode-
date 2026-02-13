class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return 0
        stack=[-1]
        max_len=0
        for i,char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    max_len=max(max_len,i-stack[-1])
        return max_len
        