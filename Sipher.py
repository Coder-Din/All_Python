alphabet =  'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

key = int(input('Write a key'))
plaintext = input('Write a sentence')
def caesar_encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        new_letter = (alphabet.find(letter.lower()) + key) % len(alphabet)
        ciphertext = ciphertext + alphabet[new_letter]
    print(ciphertext)
caesar_encrypt(plaintext, key)


cypheredtext = input('Write the cyphered text')
def anti_caesar(cypheredtext, key):
    originaltext = ''
    for letter in cypheredtext:
        original_letter = (alphabet.find(letter.lower()) - key) % len(alphabet)
        originaltext = originaltext + alphabet[original_letter]
    print(originaltext)
anti_caesar(cypheredtext, key)
