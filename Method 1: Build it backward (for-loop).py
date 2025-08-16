name = input("Enter your name: ")

rev = ""
for ch in name:
    rev = ch + rev   # put current char in front

print("Reversed:", rev)
