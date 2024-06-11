#############
# Quicksort #
#############

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = []
        middle = []
        right = []
        
        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)
        
        return quicksort(left) + middle + quicksort(right)
    
# Beispiel
arr = [2, 6, 9, 1, 14, 4, 0, 8, 8, 13]
print("Unsortierte arrste:", arr)
sorted_arr = quicksort(arr)
print("Sortierte arrste:", sorted_arr)


#############
# Mergesort #
#############

# bald..


