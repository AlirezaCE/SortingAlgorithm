import sys

def Selection_sort(arr):
    for i in range(len(A)):

        min_idx = i

        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]

if __name__ == "__main__":
  A = [64, 25, 12, 22, 11] 
  Selection_sort(A)

  print ("Sorted array")
  for i in range(len(A)):
	  print("%d" %A[i],end=" ")
