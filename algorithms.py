""" import math
import os
import random
import re
import sys

def simpleArraySum(ar):
   
    return sum(ar)

n = int(input("Enter the size of the array: "))

ar = list(map(int, input("Enter the array elements separated by space: ").split()))

if len(ar) != n:
    print("Error: The number of elements does not match the specified size.")
else:

    print("The sum of the array elements is:", simpleArraySum(ar)) """


""" #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    
    alice_score = 0
    bob_score = 0
    
   
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
    
    
    return [alice_score, bob_score]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close() """

    # Python Program to reverse an array using temporary array

# function to reverse an array
def reverseArray(arr):
    n = len(arr)
    
    # Temporary array to store elements in reversed order
    temp = [0] * n
  
    # Copy elements from original array to temp in reverse order
    for i in range(n):
        temp[i] = arr[n - i - 1]
  
    # Copy elements back to original array
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1,2,3]

    reverseArray(arr)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")







