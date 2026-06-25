class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {'}' : '{', ']' : '[', ')' : '('} 


        for c in s:
            #if we hit a close bracket, check if in stack
            if c in check:
                if stack and stack[-1] == check[c]:
                    stack.pop()
                else:
                    return False
            else: #if its open bracket we add to stack
                stack.append(c)
        


        #stack should be empty to return true
        return True if not stack else False

        

        