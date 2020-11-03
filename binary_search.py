

def binary_search(self, arr, target):
    #two pointers, going from middle
    l, r = 0, len(arr) - 1

    while l < r:
        mid = l + r // 2
        if arr[mid] == target:
            return target
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1
