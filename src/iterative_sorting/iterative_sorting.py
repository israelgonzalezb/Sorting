# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print("________")
        print(arr[i])
        print("________")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)):
            current_item = arr[i]
            compare_item = arr[j]
            print(arr[j])
            if arr[i] > arr[j]:
                print(f"{arr[i]} is bigger than {arr[j]}")
                arr[i] = compare_item
                arr[j] = current_item
            elif arr[i] < arr[j]:
                print(f"{arr[i]} is smaller than {arr[j]}")
            else:
                print(f"{arr[i]} is the same as {arr[j]}")
             

        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

print(selection_sort([1,0,0,3,5,2,0,4]))