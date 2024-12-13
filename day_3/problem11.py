#Write a program that counts the frequency of each word in a sentence using a dictionary.

def countFrequency(str):
    dict={}
    for char in str:
        if char in dict:
            dict[char]+=1
        else:
            dict[char]=1
    return dict

str="aaabbdwbbccffrkrkr"
result=countFrequency(str)
print(result)