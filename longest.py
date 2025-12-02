a = input("Enter a string:")
words = a.split()
longest = ""
for word in words:
    if len(word)>len(longest):
        longest=word
print("Longest word",longest)