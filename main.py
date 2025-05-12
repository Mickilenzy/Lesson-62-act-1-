print("Welcome to the Swanning Game! ")
print("Let's swap two numbers magically ")

# Step 1: Get input from the user
num1 = input("Enter the first number ")
num2 = input("Enter the second number")

print(f"\nBefore swapping: num1 = {num1}, num2 = {num2}")
print(" Swapping the numbers....")

#Step 2: Swapping using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Step 3: Shhow result
print(f"After swapping: num1 = {num1}, num2 = {num2}")
print(" Ta-da! The numbers have been swapped ")