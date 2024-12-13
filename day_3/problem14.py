# Write a Python program to find the key with the maximum value in a dictionary.

# Input: {"a": 10, "b": 20, "c": 15}
# Output: "b"

def minKey(dict):
    min=next(iter(dict.values()))
    print(min)
    minKey=''
    flag=0
    for key,value in dict.items():
        if value<min:
            flag=1
            min=value
            minKey=key
        if flag==0:
            minKey=next(iter(dict.keys()))     
    return minKey



dict={"a": 10, "b": 20,"d":5, "c": 15}
result=minKey(dict)
print("result -->",result)