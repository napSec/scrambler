def caesar_cipher(text, shift, mode):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26  # Ensure the shift is within the alphabet's range
            if char.islower():
                if mode == 'encrypt':
                    result += chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
                else:
                    result += chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
            elif char.isupper():
                if mode == 'encrypt':
                    result += chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
                else:
                    result += chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
        else:
            result += char  # Keep non-alphabet characters unchanged
    
    return result

# Get user input for message, shift, and mode
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter 'encrypt' or 'decrypt': ")

# Ensure the mode is valid
if mode not in ['encrypt', 'decrypt']:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
else:
    # Call the caesar_cipher function with user input
    result = caesar_cipher(message, shift, mode)
    
    print("Result:", result)
