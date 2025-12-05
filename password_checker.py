# Password Strength Checker
# This program checks if a password is strong or weak

print("=== Password Strength Checker ===")
print()

# Ask user to create a password
password = input("Create a password: ")

# Check password requirements
has_length = len(password) >= 8
has_number = any(char.isdigit() for char in password)
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)

# Display results
print()
print("Password Analysis:")
print(f"✓ At least 8 characters: {has_length}")
print(f"✓ Contains a number: {has_number}")
print(f"✓ Contains uppercase letter: {has_uppercase}")
print(f"✓ Contains lowercase letter: {has_lowercase}")
print()

# Determine if password is strong
if has_length and has_number and has_uppercase and has_lowercase:
    print("🔒 Strong Password! Your password is secure.")
else:
    print("⚠️ Weak Password! Please improve your password:")
    if not has_length:
        print("  - Make it at least 8 characters long")
    if not has_number:
        print("  - Add at least one number")
    if not has_uppercase:
        print("  - Add at least one uppercase letter")
    if not has_lowercase:
        print("  - Add at least one lowercase letter")
