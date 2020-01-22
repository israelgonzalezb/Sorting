# Insertion Sort... will need this for merge sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        print(f"{i} -----------------")
        temp_item = arr[i-1]
        print(arr)
        print(f"Currently comparing: {temp_item} and {arr[i]}")
        if temp_item > arr[i]:
            arr[i-1] = arr[i]
            arr[i] = temp_item
            print(arr)
            print(f"Switched: {temp_item} and {arr[i-1]}")
            for j in reversed(range(1,i)):
                reverse_temp = arr[j-1]
                print(f"  reverse compare: {reverse_temp} and {arr[j]}")
                if reverse_temp > arr[j]:
                    arr[j-1] = arr[j]
                    arr[j] = reverse_temp
                    print(arr)
                    print(f"  Switched: {reverse_temp} and {arr[j-1]}")
                else:
                    print(f"  {reverse_temp} and {arr[j]} are already in order")
    return arr

#insertion_sort([9,2,7,5,3,8,4])


# TO-DO: complete the helpe function below to merge 2 sorted arrays
"""
1. Create an array arr3[] of size n1 + n2.
2. Copy all n1 elements of arr1[] to arr3[]
3. Traverse arr2[] and one by one insert elements (like insertion sort) of arr3[] to arr1[]. 
This step take O(n1 * n2) time.
"""
def merge( arrA, arrB ):
    # 1. Create an array merged_arr of size n1 + n2.
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    print(f"Our array of elements of size n1 + n2 is {merged_arr} and has {len(merged_arr)} elements")
    # TO-DO
    # 2. Copy all n1 elements of arrA to merged_arr
    for i in range(len(arrA)):
        merged_arr[i] = arrA[i]
    print(f"Our merged array with items from the first array is {merged_arr}")
    # Track where arrB element was last inserted so we can skip forward
    last_insert = 0
    for k in range(len(arrB)):
        print(f"For arrB {arrB}, currently at index {k} of {len(arrB)} elements. The element is {arrB[k]}.")
        for j in range(last_insert,len(arrA)+k):
            print(f"  For merged_arr {merged_arr}, currently at index {j} of {range(last_insert,len(arrA)+k)}. The element is {merged_arr[j]}.")
            if arrB[k] < merged_arr[j]:
                print(f"    {arrB[k]} is less than {merged_arr[j]}, so insert {arrB[k]} into merged_arr, remove the last element of merged_arr and break out of this loop. We inserted at {j} so we'll set the last_insert index to {j+1}")
                last_insert = j + 1
                merged_arr.insert(j,arrB[k])
                merged_arr.pop()
                break
            if j + 1 == len(arrA)+k:
                print(f"    Sliced merged_arr ({merged_arr}) should only contain {arrA}: {merged_arr[0:j+1]}")
                merged_arr = merged_arr[0:j+1] + arrB[k:]
                print(merged_arr)
                #return merged_arr

    print(f"Merge output: {merged_arr}")
    return merged_arr

# /usr/local/opt/python/bin/python3.7 
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    test_array = []
    print("___")
    print(f"input is {arr}")
    if len(arr) <= 2:
        if len(arr) == 2:
            return merge([arr[0]],[arr[1]])
        elif len(arr) == 1:
            return merge([arr[0]],[])
        print("there are two or less items in this array")
        return arr;
    else:
        first_half = []
        second_half = []
        if len(arr)%2 == 0:
            for i in range(0,len(arr)//2):
                first_half.append(arr[i])
            for i in range(len(arr)//2,len(arr)):
                second_half.append(arr[i])
        else:
            for i in range(0,(len(arr)//2)+1):
                first_half.append(arr[i])
            for i in range((len(arr)//2)+1,len(arr)):
                second_half.append(arr[i])

        print(f"The two halves are: {first_half},{second_half}")
        #merged_arr = merge(first_half, second_half)
        #print(f"The merge function returned: {merged_arr}")
        first_half = merge_sort(first_half)
        second_half = merge_sort(second_half)

        print(f"! sorted first half: {first_half}")
        print(f"! sorted second half: {second_half}")
    final_return = merge(first_half, second_half)
    print(f"Input was: {arr}, final sort is: {final_return}")
    return final_return

#merge_sort([7,1,8])
merge_sort([38,27,43,3,9,82,10])
#merge([35,38,45],[78,79,80])

"""
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

"""

# print(merge([1,3,2,4],[3,4,7,3]))