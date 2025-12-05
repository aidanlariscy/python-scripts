# Age-Based Discount Calculator
# This program calculates discounts based on age and student status

print("=== Store Discount Calculator ===")
print()

# Get user information
age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ").lower()
purchase_amount = float(input("Enter your purchase amount: $"))

# Initialize discount
discount_percent = 0

# Determine discount based on age and student status
if age < 12 or age >= 65:
    discount_percent = 20
    print("\n✓ Child/Senior Discount Applied: 20%")
elif age >= 12 and age < 18 and student == "yes":
    discount_percent = 15
    print("\n✓ Student Discount Applied: 15%")
else:
    print("\n✗ No discount applies")

# Calculate final price
discount_amount = purchase_amount * (discount_percent / 100)
final_price = purchase_amount - discount_amount

# Display results
print(f"\nOriginal Price: ${purchase_amount:.2f}")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Final Price: ${final_price:.2f}")
