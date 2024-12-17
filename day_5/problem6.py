# Write a Python program to check if two lists have any common elements.


def commonElement(num1,num2):
    ans=[]
    for i in num1:
        if i in num2:
            ans.append(i)
    return ans

num1=[1,2,4,5,7]
num2=[2,6,9,4,5,0,8]
result=commonElement(num1,num2)
print(result)