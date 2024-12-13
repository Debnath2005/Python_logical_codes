# Given an integer array, find k'th smallest element in the array where k is a
# positive integer less than or equal to the length of array. 
# Input : [7, 4, 6, 3, 9, 1], k = 3 Output: 4
# Explanation: The 3rd smallest array element is 4 

def kthSmallestElement(lst,k):
  lst.sort()
  return lst[k-1]


lst=[7, 4, 6, 3, 9, 1]
k=3

result=kthSmallestElement(lst,k)
print(result)