def xor_cipher(s, key):
    return ''.join(chr(ord(c) ^ key) for c in s)

def main():
    encoded_text = input("Enter the text to decode: ")
    key = int(input("Enter the decryption key (integer): "))
    decoded_text = xor_cipher(encoded_text, key)
    print(f"Decoded text: {decoded_text}")

if __name__ == "__main__":
    main()
