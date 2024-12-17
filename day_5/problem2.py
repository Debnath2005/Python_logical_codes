# Write a program to count the frequency of each word in a given string.
# Example: "hello world hello" → {'hello': 2, 'world': 1}.

def findFreq(str):
    words = str.split()

    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

str="hello world hello"
result=findFreq(str)
print(result)