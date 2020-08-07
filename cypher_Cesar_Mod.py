alphabet =  'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
banned = [3, 6, 9, 11, 12, 15, 18, 21, 22, 24, 27, 30, 33]
key1 = int(input('Write a key1'))

key1bool = False
key2bool = False
while key1bool == False:
    for elem in banned:
        if key1 == elem:
            key1 = int(input('Write a key1 AGAIN!!!'))
            key1bool = False
            break
        else:
            key1bool = True
key2 = int(input('Write a key2'))
while key2bool == False:
    for elem in banned:
        if key2 == elem:
            key2 = int(input('Write a key2 AGAIN!!!'))
            key2bool = False
            break
        else:
            key2bool = True
plaintext = input('Write a sentence')
def caesar_encrypt(plaintext, key1, key2):
    ciphertext = ''
    for letter in plaintext:
        new_letter = (alphabet.find(letter) * key2 + key1) % len(alphabet)
        ciphertext = ciphertext + alphabet[new_letter]
    print(ciphertext)
caesar_encrypt(plaintext, key1, key2)             

cypheredtext = input('Write the cyphered text')
def anti_caesar(cypheredtext, key1, key2):
    originaltext = ''
    for letter in cypheredtext:
        original_letter = int((alphabet.find(letter) - key1)/key2 % len(alphabet))
        originaltext = originaltext + alphabet[original_letter]
        '''print(key1)
        print(key2)
        print(alphabet.find(letter))
        print(alphabet[original_letter])'''
    print(originaltext)
anti_caesar(cypheredtext, key1, key2)

