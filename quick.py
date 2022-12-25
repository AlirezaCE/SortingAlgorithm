# Function to find the partition position
def place(a, low, high):
  
    down = low
    up = high

    while down<up:
        while down < len(a) and a[down] <= a[low]:
            down += 1

        while up > -1 and a[up] > a[low]: 
            up -= 1
        if down < up:
            a[down], a[up] = a[up], a[down]

    a[low], a[up] = a[up], a[low] 
    # a , b
    # temp = a
    # a = b 
    # b = temp
    #swap(a[low], a[up])
    return up    
  
def quick_sort(a, low, high):
    if low < high:
  
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        j = place(a, low, high)
  
        # Recursive call on the left of pivot
        quick_sort(a, low, j - 1)
  
        # Recursive call on the right of pivot
        quick_sort(a, j + 1, high)
  
  
# Driver code
a = [10, 7, 8, 9, 1, 5, 234]

quick_sort(a, 0, len(a) - 1)
  
print(f'Sorted array: {a}')
  
# This code is contributed by Adnan Aliakbar
