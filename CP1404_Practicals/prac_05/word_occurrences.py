"""
Word Occurrences
Estimate: 15 minutes
Actual:   18 minutes
"""

text=input("Text: ")
words=text.split(" ")
words.sort()
count=0
for i in words:
    if len(i) > count:
        count = len(i)
        longest_word = i

# longest_word=max(words, key=len)
count_of_words={}
for i in words:
    count_of_words[i]=words.count(i)

for i in count_of_words:
    print(f"{i:{len(longest_word)}} : {count_of_words[i]}")
print()
