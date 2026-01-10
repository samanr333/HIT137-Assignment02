# Create a program that reads the text file "raw_text.txt", encrypts its contents using a
# simple encryption method, and writes the encrypted text to a new file
# "encrypted_text.txt". Then create a function to decrypt the content and a function to
# verify the decryption was successful.

# Encryption function
def encryption(shift1, shift2):
    # Reading data from raw_text.txt file
    with open("raw_text.txt", "r") as f:
        input_txt = f.read()
    # Initialising a string that stores the encrypted text
    encrypted_text = ""

    # Encryption logic
    # The ord() function takes the character and converts it to its corresponding ASCII value
    # The chr() function takes ASCII value and converts it to corresponding character
    for ch in input_txt:
        if ch.islower():
            if ch <= 'm':
                encrypted_text += chr((ord(ch) - 97 + (shift1 * shift2)) % 26 + 97)
            else:
                encrypted_text += chr((ord(ch) - 97 - (shift1 + shift2)) % 26 + 97)

        elif ch.isupper():
            if ch <= 'M':
                encrypted_text += chr((ord(ch) - 65 - shift1) % 26 + 65)
            else:
                encrypted_text += chr((ord(ch) - 65 + (shift2 * shift2)) % 26 + 65)

        else:
            encrypted_text += ch
    # Creating a text file with the encrypted text
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted_text)

# Decryption function
def decryption(shift1, shift2):
    with open("encrypted_text.txt", "r") as f:
        input_txt = f.read()

    decrypted_text = ""
    for ch in input_txt:
        if ch.islower():
            if ch <= 'm':
                decrypted_text += chr((ord(ch) - 97 - (shift1 * shift2)) % 26 + 97)
            else:
                decrypted_text += chr((ord(ch) - 97 + (shift1 + shift2)) % 26 + 97)

        elif ch.isupper():
            if ch <= 'M':
                decrypted_text += chr((ord(ch) - 65 + shift1) % 26 + 65)
            else:
                decrypted_text += chr((ord(ch) - 65 - (shift2 * shift2)) % 26 + 65)

        else:
            decrypted_text += ch

    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted_text)

    return decrypted_text

# Review function that checks if the decrypted text and the raw text file are same or not
def review():
    # Reading the data of encrypted_text.txt and decrypted_text.txt
    with open("raw_text.txt", "r") as raw, open("decrypted_text.txt", "r") as dec:
        raw_text = raw.read()
        decrypted_text = dec.read()
        if raw_text == decrypted_text:
            print("Decryption successful")
        else:
            print("Decryption unsuccessful")
