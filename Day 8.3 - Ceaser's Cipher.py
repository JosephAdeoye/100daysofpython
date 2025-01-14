alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
ascii_art = """
   _____  ______   ______   ______   _____   ____   _____  
  /  ___||  _   | |  _   | |  ____| |  ___| |  _ \\ |  _  \\ 
 |  |    | |_|  | | |_|  | | |__    | |___  | |_| || |_|  |
 |  |    |  _   | |  _   | |  __|   |  ___| |  _  ||  _  / 
 |  |___ | | |  | | | |  | | |____  | |     | | | || | \\ \\ 
  \\____/ |_| |_| |_| |_|  |_|______||_|     |_| |_||_|  \\_\\
"""
print(ascii_art)
print("Welcome to Ceaser's Cipher!")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()

if direction not in ["encode", "decode"]:
    print("Invalid input. Please enter either 'encode' or 'decode' ")
    exit()
else:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            encrypted_text += alphabet[new_position]
    print(f"The encrypted text is: {encrypted_text}")

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            decrypted_position =  (position - shift) % 26
            decrypted_text += alphabet[decrypted_position]
    print(f"The decrypted text is: {decrypted_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("That is an invalid input. Please enter either 'encode' or 'decode' ")

