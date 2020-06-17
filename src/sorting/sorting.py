# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # Your code here
    merged_arr = []
    # create index counter
    ai = 0
    bi = 0
    # while there's stuff in the arrays
    while ai < len(arrA) or bi < len(arrB):
        # if smaller, add it to merged list, move to next index
        if bi >= len(arrB):
            merged_arr.append(arrA[ai])
            ai += 1
        elif ai >= len(arrA):
            merged_arr.append(arrB[bi])
            bi += 1
        elif arrA[ai] < arrB[bi]:
            merged_arr.append(arrA[ai])
            ai += 1
        else:
            merged_arr.append(arrB[bi])
            bi += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # if len(arr) >= 1:
    #     pass
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    l = arr[:mid]
    r = arr[mid:]
    return merge(merge_sort(l), merge_sort(r))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

    # while elements > 0:
    #     if len(arrA) == 0:
    #         merged_arr.extend(arrB)
    #         arrB = []
    #     elif len(arrB) == 0:
    #         merged_arr.extend(arrA)
    #         arrA = []
    #     elif arrA[0] > arrB[0]:
    #         merged_arr.append(arrB.pop(0))
    #     else:
    #         merged_arr.append(arrA.pop(0))

    #     elements = len(arrA) + len(arrB)
