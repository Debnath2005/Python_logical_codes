# Target Sum

def findSum(my_set,target):
  low=0
  high=len(my_set)-1

  while low<high:
    if my_set[low]+my_set[high]==target:
      return low,high
    elif my_set[low]+my_set[high]>target:
      high-=1
    else:
      low+=1


my_set=[2,1,11,15]
target=3

result=findSum(my_set,target)
print(result)