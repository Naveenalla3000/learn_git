def palindrome(arr):
    left,right=0,len(arr)-1
    while left<right :
        arr[left],arr[right]=arr[right],arr[left]
        left +=1
        right -=1
    return arr
array=[1,2,3,4,3,5,5,5]
original=array[:]
if (original == palindrome(array)) :
    print("True")
else :
    print("False")
