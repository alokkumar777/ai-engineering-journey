def caesar(text, shift, encrypt=True):
  if not isinstance(shift, int):
    return 'Shift should be an integer'
  
  if shift < 1 or shift > 25:
    return 'Shift should be in between 1 to 25'
  
  if not encrypt:
    shift = -shift

  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  shifted_alpha = alphabet[shift:] + alphabet[:shift]
  translation_table = str.maketrans(alphabet + alphabet.upper(),shifted_alpha + shifted_alpha.upper())
  encrypted_text = text.translate(translation_table)
  return encrypted_text

def encrypt(text, shift):
  return caesar(text, shift)

def decrypt(text, shift):
  return caesar(text, shift, False)

encrypted_text = encrypt('SuperCoder', 3)
print("Encrypt: ", encrypted_text)

decrypted_text = decrypt('VxshuFrghu', 3)
print("Decrypt: ", decrypted_text)