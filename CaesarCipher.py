def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").upper()
        if choice in ['E', 'D']:
            message = input("Enter your message: ")
            try:
                shift = int(input("Enter the shift value: "))
            except ValueError:
                print("Shift value must be an integer.")
                continue

            if choice == 'E':
                encrypted_message = caesar_cipher(message, shift, encrypt=True)
                print(f"Encrypted Message: {encrypted_message}")
            else:
                decrypted_message = caesar_cipher(message, shift, encrypt=False)
                print(f"Decrypted Message: {decrypted_message}")
            
            break
        else:
            print("Invalid choice, please select (E) or (D).")

if __name__ == "__main__":
    main()
