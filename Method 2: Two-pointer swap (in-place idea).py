name = list(input("Enter your name: "))
i, j = 0, len(name) - 1

while i < j :
    name[i], name [j] = name[j], name[i]
    i += 1
    j -= 1

print("Reversed: ", "".join(name))