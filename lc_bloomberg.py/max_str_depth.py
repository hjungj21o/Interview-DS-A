# find string at highest depth e.g., ((AB)(((CD)))) return depth 4 and string = CD


def max_depth(str):
    depth = 0
    max_depth = 0
    best_start = 0
    best_end = 0

    for i, char in enumerate(str):
        if char == '(':
            depth += 1
            if depth > max_depth:
                max_depth = depth
                best_start = i + 1
        elif char == ')':
            if depth == max_depth:
                best_end = i
            depth -= 1

    return str[best_start:best_end]

"""
    Stack problem using pointers

    have depth, max_depth pointing to 0
    have best_start and best_end point to 0 (these will be our end indices)

    iterate through str:
        if char is an open paren,
            we increment the depth by 1
            do another check to see if depth > max_depth. if it is, replace max_depth with depth
            mark best_start index with i + 1
        elif char is a closed paren,
            decrement depth by 1
            if depth == max_depth set by open paren, best_end idx == i

    return str[best_start:best_end]

"""




print(max_depth('((AB)(((CD))))'))
