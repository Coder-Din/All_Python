alphabet =  'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
plaintext = input('Write the text you want to cypher')
def cypher(plaintext):
    cyphered_text = ''
    for letter in plaintext:
        new_letter = 32 - alphabet.find(letter.lower())
        cyphered_text = cyphered_text + alphabet[new_letter]
    print(cyphered_text)
cypher(plaintext)
cypheredtext = input('Write the cyphered text')
def anticypher(cypheredtext):
    originaltext = ''
    for letter in cypheredtext:
        origletter = 32 - alphabet.find(letter.lower())
        originaltext = originaltext + alphabet[origletter]
    print(originaltext)
anticypher(cypheredtext)
        
