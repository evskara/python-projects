# add support for uppercase and punctuation

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

ciphertext = ''

print("Please enter the text you want to encrypt.")
plaintext = input().lower()
print("And please enter the key (how far you want the alphabet to be shifted).")
key = int(input())

for character in plaintext:
    if character == " ":
        newletter = " "
        ciphertext = ciphertext + newletter
    else:
        position = alphabet.index(character)
        newposition = position + key
        if newposition > 25:
            newposition = newposition % 26
        newletter = alphabet[newposition]
        ciphertext = ciphertext + newletter

print("Your text unencrypted is:", plaintext)
print(" ")
print("After encryption, it's:", ciphertext)
print(" ")
print("And in all caps:", ciphertext.upper())
