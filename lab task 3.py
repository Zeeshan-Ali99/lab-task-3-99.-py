"""PROGRAM:01"""

total=0
for i in range(5):
    marks=input("Enther the marks:")
    marks = int(marks)
    total =  total + marks

percentage = total/5
print("total marks =",total)

if percentage >=80:
   print("Grade = A")
elif percentage >=70:
   print("Grade = B")
elif percentage >=60:
    print("Grade = C")  
elif percentage >= 50:
    print("Grade = D")
else:
   print("Grade = F")

if percentage >=50:
   print("pass")
else:
    print("fail") 



"""PROGRAM:02"""

name = "Zeeshan Ali"

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Number of characters:", len(name))
print("First character:", name[0])
print("Last character:", name[-1])


"""PROGRAM:03"""

numbers = []

# Ask the user to enter 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Calculations
total = sum(numbers)
average = total / 10
largest = max(numbers)
smallest = min(numbers)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display results
print("\n--- Results ---")
print("Sum:", total)
print("Average:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count) 


"""PROGRAM:04"""


balance = 50000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        balance = balance + amount
        print("Deposit successful.")
        print("Your new balance is:", balance)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Your remaining balance is:", balance)
        else:
            print("Insufficient balance.")

    elif choice == 4:
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice. Please try again.")


"""PROGRAM:05"""


n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print("\nMultiplication Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)