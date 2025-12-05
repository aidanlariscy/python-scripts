# Grade Calculator
# This program calculates the average grade and assigns a letter grade

print("=== Grade Calculator ===")
print()

# Ask user how many assignments they have
num_assignments = int(input("How many assignments do you have? "))

# Initialize total to 0
total = 0

# Get each grade and add to total
for i in range(num_assignments):
    grade = float(input(f"Enter grade for assignment {i + 1}: "))
    total += grade

# Calculate average
average = total / num_assignments

# Display average
print()
print(f"Your average grade is: {average:.2f}")

# Determine letter grade
if average >= 90:
    print("Letter Grade: A - Excellent work!")
elif average >= 80:
    print("Letter Grade: B - Good job!")
elif average >= 70:
    print("Letter Grade: C - Keep working!")
elif average >= 60:
    print("Letter Grade: D - Need improvement")
else:
    print("Letter Grade: F - Please see your instructor")
