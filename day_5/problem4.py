# Write a Python program to find all pairs of integers in a list whose sum is equal to a given number.
# Example: [1, 2, 3, 4, 5] with target 6 → [(1, 5), (2, 4)].

def targetSum(num,target):
    ans=[]
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i]+num[j]==target:
                 ans.append((num[i], num[j]))
    return ans
num=[1, 2, 3, 4, 5]
target=6
result=targetSum(num,target)
print(result)