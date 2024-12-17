# Write a Python program to remove duplicates from a list while preserving the order.


# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

def removeDuplicate(num):
    ans=[]
    for i in num:
        if i not in ans:
            ans.append(i)
    return ans


num=[1, 2, 2, 3, 4, 4, 5, 5 ,6 ,6 ,7]
result=removeDuplicate(num)
print(result)