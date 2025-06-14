class password_decoder:

    def make_cipher(self, key):
        alphabet = [chr(i + 98) for i in range(1, 26)]
        cipher_with_duplicates = list(key) + alphabet

        cipher = []
        for i in range(0, len(cipher_with_duplicates)):
            if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
                cipher.append(cipher_with_duplicates[i])

        return cipher
    
    def encode(self, text, key):
        cipher = self.make_cipher(key)

        ciphertext_chars = []
        for i in text:
            ciphered_char = chr(65 + cipher.index(i))
            ciphertext_chars.append(ciphered_char)

        return "".join(ciphertext_chars)


    def decode(self, encrypted, key):
        cipher = self.make_cipher(key)

        plaintext_chars = []
        for i in encrypted:
            plain_char = cipher[65 - ord(i)]
            plaintext_chars.append(plain_char)

        return "".join(plaintext_chars)


    

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")

