def encrypt(text):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    crypt_phrase = ""

    for i in range(len(text)):
        
        char = text[i].lower()

        # doesn't encrypt special characters
        if char not in alphabet:
            crypt_phrase += char
            continue

        shift_index = alphabet.find(char) + 5
        shift_letter = alphabet[shift_index % 26]
        
        crypt_phrase += shift_letter

    print(f"The encrypted message is: {crypt_phrase}")
    print("FYI: The cipher has a shift of 5")


phrase = input("Please enter a sentence: ")

encrypt(phrase)

