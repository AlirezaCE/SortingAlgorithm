def bubbleSort_not_optimization(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            count += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    print("count = %d" %count)


def bubbleSort_optimized(arr):
    count = 0 
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            count += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                

    print("count = %d" %count)


def bubbleSort_optimized_and_check_array_isSorted(arr):

    count1 = 0

    n = len(arr)
    swapped = False
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            count1 += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                

        if swapped == False:
            break
    
    print("count = %d" %count1)

def print_bubble(arr):
    print("Sorted array is:")
    for i in range(len(arr)):
      print("%d" % arr[i], end=" ")
    print("\n")


if __name__ == "__main__":

  arr1 = arr2 = arr3 = [4, 1, 2, 3, 5]

  bubbleSort_not_optimization(arr1)
  print_bubble(arr1)

  bubbleSort_optimized(arr2)
  print_bubble(arr2)

  bubbleSort_optimized_and_check_array_isSorted(arr3)
  print_bubble(arr3)


