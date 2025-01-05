import math
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

    print("The sum of the array elements is:", simpleArraySum(ar))







