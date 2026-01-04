text = 'hello'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shifted_alpha = alphabet[shift:] + alphabet[:shift]
translation_table = str.maketrans(alphabet,shifted_alpha)
encrypted_text = text.translate(translation_table)
print(encrypted_text)   