# 1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
# a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
# b. Logic -> Replace <<UserName>> with the proper name
# c. O/P -> Print the String with User Name

userName = input("Enter a user name: ")

if len(userName) >= 3:  
    print(f"Hello {userName}, How are you?") 
else:
    print("UserName is required to have a minimum of 3 characters.")
