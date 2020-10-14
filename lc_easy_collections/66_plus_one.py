class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        step = 0

        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                num = digits[i] + 1
            else:
                num = digits[i] + step

            if num < 10:
                digits[i] = num
                step = 0
                break
            else:
                digits[i] = num % 10
                step = num // 10

        if step == 1:
            digits.insert(0, 1)

        return digits


"""
    go backwards?
    if num > 10... so we should replace the num with % 10. and have a step that toggles 0 and 1
    
    iterate backwards of input list
        add one to the last array
        if it's less than 10, break
        if it's 10, then that num should be num % 10
        have a step - divide by 10
    return digits
"""
