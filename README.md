# XOR Encryption/Decryption

This project demonstrates a simple XOR cipher for encoding and decoding text. XOR encryption is a symmetric key encryption technique where the same key is used for both encryption and decryption.

## Files

- `xor_encoder.py`: Script for encoding text using the XOR cipher.
- `xor_decoder.py`: Script for decoding text using the XOR cipher.

## Usage

### Encoding

1. Run the encoder script:
    ```bash
    python xor_encoder.py
    ```
2. Enter the text you want to encode.
3. Enter the encryption key (an integer).

The script will output the encoded text.

### Decoding

1. Run the decoder script:
    ```bash
    python xor_decoder.py
    ```
2. Enter the text you want to decode.
3. Enter the decryption key (an integer).

The script will output the decoded text.

## Example

### Encoding Example

```bash
$ python xor_encoder.py
Enter the text to encode: Hello, World!
Enter the encryption key (integer): 123
Encoded text: ϮϢϢϩϧϧϧϢϧϯϧϦϨϢ
```

### Decoding Example

```bash
$ python xor_decoder.py
Enter the text to decode: ϮϢϢϩϧϧϧϢϧϯϧϦϨϢ
Enter the decryption key (integer): 123
Decoded text: Hello, World!
```


