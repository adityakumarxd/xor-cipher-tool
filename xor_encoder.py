def xor_cipher(s, key):
    return ''.join(chr(ord(c) ^ key) for c in s)

def main():
    plaintext = input("Enter the text to encode: ")
    key = int(input("Enter the encryption key (integer): "))
    encoded_text = xor_cipher(plaintext, key)
    print(f"Encoded text: {encoded_text}")

if __name__ == "__main__":
    main()
