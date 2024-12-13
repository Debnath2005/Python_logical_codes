# Merge two dictionaries and sum the values of keys that exist in both.

# Input: dict1 = {"a": 1, "b": 2}, dict2 = {"b": 3, "c": 4}
# Output: {"a": 1, "b": 5, "c": 4}

def combinedTwoDict(dict1,dict2):
    newDict={}
    newDict=dict1.copy()
    for key,value in dict2.items():
        if key in newDict:
            newDict[key]+=value
        else:
            newDict=value
    print(newDict)
    return newDict



dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
result=combinedTwoDict(dict1,dict2)
print(result)