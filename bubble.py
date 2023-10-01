def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize by detecting if any swaps were made in this pass
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps were made in a pass, the array is already sorted
        if not swapped:
            break
    return arr

# Input array
input_array = [5, 2, 9, 1, 5, 6]

# Sorting the array using Bubble Sort
sorted_array = bubble_sort(input_array)
print("Sorted Array:", sorted_array)