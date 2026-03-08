"""
1. Given a sorted array A (sorted in ascending order), having N integers, find if there exists any ir of elements (ALl, Alil) such that their sum is equal to X.
For Example: A[] = (10, 20, 35, 50, 75, 80) and the value of X = 110
"""

target = 1100 
arr = [10,20,35, 50, 75, 80]

i = 0
j = len(arr)-1
found = False
while(i < j) :

    if arr[i] + arr[j] == target:
        found = True
        print(1)
        break
    elif arr[i] + arr[j] < target:
        i += 1
    elif arr[i] + arr[j] > target:
        j -= 1

if not found:
    print(-1)
    
