# Write a Python program to find the top 3 highest values in a dictionary.
# Example: {'a': 5, 'b': 2, 'c': 8, 'd': 3} → [8, 5, 3].

def hightestFreq(dict):
    ans=[]
    result=[]
    for key,value in dict.items():
        ans.append(value)
    ans.sort(reverse=True)
    for j in range(3):
        result.append(ans[j])
    return result



dict={'a': 5, 'b': 2, 'c': 8, 'd': 3}
result=hightestFreq(dict)
print(result)