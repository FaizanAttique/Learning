#user's name
name = input("Enter your name: ")

#ask three numbers
numbers = []
for i in range(1, 4):
    number = int(input(f"Enter your {i} favorite number: "))
    numbers.append(number)

# Greet user with name
print(f"\nHello, {name}! Let's explore your favorite numbers:")

# Check if numbers are even or odd and store in a list of tuples
parity_list = []
for number in numbers:
    if number % 2 == 0:
        parity_list.append((number, "even"))
    else:
        parity_list.append((number, "odd"))

# Print whether each number is even or odd
for number, parity in parity_list:
    print(f"The number {number} is {parity}.")

# Create and print tuples of numbers and their squares
print()
for number in numbers:
    square_tuple = (number, number ** 2)
    print(f"The number {number} and its square: {square_tuple}")

# Calculate sum of the three numbers
sum_numbers = sum(numbers)

# Print the sum with message
print(f"\nAmazing! The sum of your favorite numbers is: {sum_numbers}")

# check if the sum is a prime number
is_prime = True
if sum_numbers <= 1:
    is_prime = False
else:
    for i in range(2, int(sum_numbers ** 0.5) + 1):
        if sum_numbers % i == 0:
            is_prime = False
            break

# Notify user if sum is a prime number
if is_prime:
    print(f"Wow, {sum_numbers} is a prime number!")
else:
    print(f"{sum_numbers} is not a prime number, but it’s still a great number!")