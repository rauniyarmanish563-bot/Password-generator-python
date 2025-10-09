import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # Base character set: lowercase letters
    characters = string.ascii_lowercase

    # Add more character types based on user choices
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Ensure there's at least one character to choose from
    if not characters:
        return "Error: No character types selected."

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator 🔐")

    # Get desired password length
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number for the length.")
        return

    # Get complexity preferences
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols (e.g., @, #, $)? (y/n): ").lower() == 'y'

    # Generate and display password
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
