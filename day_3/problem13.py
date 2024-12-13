# Convert a dictionary into two lists: one containing the keys and the other containing the values.
# Input: {"a": 1, "b": 2, "c": 3}
# Output: keys = ["a", "b", "c"], values = [1, 2, 3]

def printKeyValue(Input):
    keys=[]
    values=[]
    for key,value in Input.items():
        keys.append(key)
        values.append(value)
    return keys,values

Input= {"a": 1, "b": 2, "c": 3}
key,value=printKeyValue(Input)
print("Keys:", key)
print("Values:", value)