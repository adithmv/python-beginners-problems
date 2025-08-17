numbers = []

for i in range(10):
    numbers.append(int(input(f"Number {i+1}: ")))

even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = len(numbers) - even_count

print("Numbers entered:", numbers)
print("Even count:", even_count)
print("Odd count:", odd_count)
