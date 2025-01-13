alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += char
    return encrypted_text
    # print(f"The encrypted text is: {encrypted_text}")

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            decrypt_position = (position - shift) % 26
            decrypted_text += alphabet[decrypt_position]
        else:
            decrypted_text += char
    return decrypted_text
    # print(f"The decrypted text is: {decrypted_text}")

# Normalize user input to handle case sensitivity and whitespace
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("You did not enter a valid input! Please enter 'encode' or 'decode'.")
