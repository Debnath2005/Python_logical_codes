# Write a program to split a list into sublists of size n.
# Example: [1, 2, 3, 4, 5, 6] with n=2 → [[1, 2], [3, 4], [5, 6]].

def splitList(num,n):
    result=[]
    for i in num:
        res=[]
        for j in range(0,len(n)+1):
            res.append(j)
        result.append(res)
        res=[]
    return result

num= [1, 2, 3, 4, 5, 6]
n=2

result=splitList(num,n)
print(result)