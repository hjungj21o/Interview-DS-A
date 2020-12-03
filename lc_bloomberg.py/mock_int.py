# """
# Given a string, for each repeating characters, compress the string

# aabbccc => a2b2c3

# two pointers
# counter that would increment 

# have a hash
# key will be the character, value would be the count 
# "a": 2  => a2
# stringify value, concatenate it at the end
# """


# """
# Given a string, every consecutive char with >= 3, crush it
# repeat until no consec chars left

# ex:
# "aaabbbc" => "c"
# "aabbbacd" => "cd"

# stack = [[char, count]] aa => ["a", 2]
# main logic:
#     if char == the last element in the stack:
#         increment the count: ["a", 3] "aaa" 
#     else:
#         if count >= 3:
#             pop()
        
        
#         either append OR pop the char, 

#     after we iterate through the string, if last count in stack >= 3: 
#         pop it ["a", 3]

#     res = []
#     for char, count in stack: [c, 2]
#         append(char * count) "cc"

# Time: O(N)
# Space: O(N)

# Unit tests:
# 1. check if length of string is < 3, what should it return? 
# 2. check large string length
# 3. check where there's no crushing happening
# """

# def candy_crush(str):
#     if len(str) < 3: return str

#     stack = [] #[char, count] 

#     for char in str:  # "caaa" [[c, 1], [a, 3]]
#         if stack and char == stack[-1][0]: 
#             stack[-1][1] += 1
#         else:
#             if stack and stack[-1][1] >= 3:
#                 stack.pop()  #"aa" d
#             if stack and char == stack[-1][0]:
#                 stack[-1][1] += 1
#             else:
#                 stack.append([char, 1])

#     if stack and stack[-1][1] >= 3: #"aaa"
#         stack.pop()

#     res = []
#     for char, count in stack:
#         res.append(char * count)

#     return ("").join(res) #c


# print(candy_crush("aaabbbc"))
# print(candy_crush("aaabbbc"))
# # // "c"
# print(candy_crush("aabbbacd"))
# # // "cd"
# print(candy_crush("aabbccddeeedcba"))
# # // ""
# print(candy_crush("aaabbbacd"))
# # //"acd"
# print(candy_crush("aaaaawefbbbffaasbtrcd"))
# # //"weaasbtrcd". Covers greedy approach
"""
Given a singly linked list, group all of the even nodes together followed by odd nodes

1 -> 2 -> 3 -> 4 -> 5
looking at values
6 -> 10 -> 14 -> 3 -> 11 -> 1
                              c
           o

2 pointers
perform a value swap

have a curr pointer that traverses thru the entire LL
have a odd poitner that traverses only when curr hits a value that isn't odd
curr.val, odd.val = odd.val, curr.val


1 -> 2 -> 3 -> 4 -> 5
o    e
1 -> 3 -> 5 -> 2 -> 4
head = None

head = head pointer for odd nodes
even_head = head pointer for even (aka head.next)

odd = head
even = head.next

while even and even.next:
    odd.next = even's next
    move odd up

    even.next = odd.next
    move even up

odd's next => even's head

return head
"""


"""
my_pow: x, n 
n can be either positive or negative 
neg = 1 / x ^ n

suboptimal way:
    recursively call x * my_pow(x, n - 1) until n = 0
Time: O(N)
Space: O(1)

Time: O(log N)
helper function:
    if n == even, my_pow(x, n // 2) * my_pow(x, n // 2) == my_pow(x , n)
    odd, my_pow(x, n // 2) * my_pow(x, n // 2) * x
"""
