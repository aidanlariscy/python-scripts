# Sleep Calculator
# This program checks if you got enough sleep based on your age

print("=== Sleep Calculator ===")
print()

# Ask user for sleep information
hours_slept = float(input("How many hours did you sleep last night? "))
age = int(input("What is your age? "))

# Determine recommended sleep based on age
if age < 18:
    recommended_sleep = 9
    print(f"\nRecommended sleep for your age: {recommended_sleep} hours")
else:
    recommended_sleep = 8
    print(f"\nRecommended sleep for your age: {recommended_sleep} hours")

# Calculate the difference
difference = hours_slept - recommended_sleep

# Display results
print(f"You slept: {hours_slept} hours")
print()

# Give feedback based on sleep
if difference >= 0:
    print("✓ Great job! You got enough sleep!")
    if difference > 2:
        print("You might have slept a bit too much, but rest is important!")
elif difference >= -1:
    print("⚠️ Close! Try to get a bit more sleep tonight.")
else:
    print("❌ You need more sleep! Try to go to bed earlier tonight.")
    print(f"You were short by {abs(difference):.1f} hours.")
