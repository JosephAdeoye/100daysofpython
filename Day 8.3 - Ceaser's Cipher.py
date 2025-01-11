alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Don't change the code above

# TODO 1 - Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO 2 - Inside the 'encrypt' function, shift each letter of the 'text' forward in the alphabet by the shift amount and print the encrypted text.

# TODO 3 - Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a messagee

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_postion = (position + shift) % 26
            encrypted_text += alphabet[new_postion]
        else:
            encrypted_text += char
    print(f"The encrypted text is {encrypted_text}")

encrypt(text, shift)


   