# 2. Reverse Words in a String
# Write a function reverse_words that takes a string s and returns the string with each word reversed 
# but the order of the words preserved.

# reverse_words("Let's take LeetCode contest")
# Output: "s'teL ekat edoCteeL tsetnoc"
def reverse_word(word):
    return ''.join(reversed(word))

def reverse_words(s):
    word_list = s.split(' ')
    reversed_words = []
    for word in word_list:
        reversed_words.append(reverse_word(word))
    
    return ' '.join(reversed_words)


str="Let's take LeetCode contest"
result=reverse_words(str)
print(result)
