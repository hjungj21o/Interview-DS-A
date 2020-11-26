# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
        #         stack = []

        #         for i in range(len(s)):
        #             if not stack or stack[-1][0] != s[i]:
        #                 stack.append([s[i], 1])
        #             else:
        #                 stack[-1][1] += 1
        #                 if stack[-1][1] == k:
        #                     stack.pop()

        #         res = []
        #         for char, num in stack:
        #             res.append(char * num)

        #         return ''.join(res)

        # stack = []
        # counter_stack = []

        # for char in s:
        #     if not stack or stack[-1] != char:
        #         stack.append(char)
        #         counter_stack.append(1)
        #     else:
        #         counter_stack[-1] += 1
        #     if counter_stack[-1] == k:
        #         stack.pop()
        #         counter_stack.pop()

        # return "".join([stack[i] * counter_stack[i] for i in range(len(stack))])


"""
    1 stack approach:
        create a stack
        
        iterate through str:
            if stack is empty or last ele in stack and s[i] are diff:
                append [char, 1] to stack
            else:
                increment last ele in stack by 1
            if last ele in last ele in stack == k:
                pop it off the stack
                
        create a res list (because string is immutable, it's better to create a list)
        iterate through stack:
            append into res char * num
            
        return joined result
        
    2 stack approach:
        create a stack and a counter_stack (keep count of num of characters)
        iterate through str:
            if stack is empty or last ele in stack != char:
                append char into stack, 1 to counter_stack
            else:
                increment last ele of counter_stack
            if counter_stack[-1] == k:
                pop stack and counterstack
        create a list
        iterate through stack and counter stack, stack[i] * counter_stack[i]
        join them together

"""



def candy_crush1(s):
    stack = []

    for char in s: 
        if stack:
            if char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                if stack[-1][1] >= 3:
                    stack.pop()
                if stack and stack[-1][0] == char:
                    stack[-1][1] += 1
                else:
                    stack.append([char, 1])
        else:
            stack.append([char, 1])

    if stack[-1][1] >= 3:
        stack.pop()

    res = []
    for char, num in stack:
        res.append(char * num)
    return "".join(res)


def candy_crush2(s):
    stack = []

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            if stack and stack[-1][1] >= 3:
                stack.pop()
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
    
    if stack[-1][1] >= 3:
        stack.pop()
    
    res = []
    for char, num in stack:
        res.append(char * num)
    return "".join(res)


# print("hello")
# print(candy_crush("aaabbbc"))
print(candy_crush1("aaabbbbc"))
print(candy_crush2("aaabbbbc"))
# print(candy_crush("aabbbacd"))
print(candy_crush1("aabbccddeeedcbax"))
print(candy_crush2("aabbccddeeedcbax"))
