def dublicateChar(str1):
  ans={}
  for char in str1:
    if char in ans:
      ans[char]+=1
    else:
      ans[char]=1


  result=[]
  for key,value in ans.items():
    if value>1:
      result.append(key)

  return result



str1="aabcdde"
result=dublicateChar(str1)
print(result)