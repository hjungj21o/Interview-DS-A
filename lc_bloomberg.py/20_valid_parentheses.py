class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        stack = []

        pair = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        for char in s:
            if char in pair:
                if not stack or pair[char] != stack.pop():
                   return False
            else:
                stack.append(char)
            print(stack)
        return len(stack) == 0


"""
    stack problem
    
    create a stack
    create a dictionary, key being the closing parens and values being open parens
    
    iterate through s:
        if char is a key in dict:
            check for two conditions: if stack is empty (meaning the first char is closed paren) or if the value does not equal the last element in stack(diff paren pairs):
            return False
        else:
            it must mean we've hit open parens, so append char
            
    return True or False by checking if length of stack is 0.

"""
