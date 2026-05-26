def find_max_min(arr):
    if not arr:
    # Return None for both if the array is empty
        return None, None  
    #if one element in the array, return that element as both max and min
    if len(arr) == 1:
        return arr[0], arr[0]
        
    #if in array of two elements, compare them and return the max and min
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    #find the middle index of the array
    mid = len(arr)//2

    #recursively find the max and min in the left half of the array
    left_max, left_min = find_max_min(arr[:mid])
    right_max, right_min = find_max_min(arr[mid:])

    #compare the max and min from both halves and return the overall max and min
    final_min = left_min if left_min < right_min else right_min
    final_max= left_max if left_max > right_max else right_max
    return final_max, final_min

if __name__ == "__main__":
        test_array = [3, 1, 4, 1, 5, 9, 2, 6]
        max_value, min_value = find_max_min(test_array)
        print(f"First Array: {test_array}")
        print(f"Result: Max: {max_value}, Min: {min_value}")
        print(f"Type returned value: {type((max_value, min_value))}")
