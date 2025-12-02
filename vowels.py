text = input("Enter a string:")

vowels = 0
consonent = 0
digit = 0
spaces = 0

for char in text:
    if char.lower() in "aeiou":
        vowels+=1
    elif char.isalpha():
        consonent+=1
    elif char.isdigit():
        digit+=1
    elif char.isspace():
        spaces+=1

print("Vowels:",vowels)
print("Consonent",consonent)
print("Digit",digit)
print("Spaces",spaces)