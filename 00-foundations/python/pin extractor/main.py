# Build a pin extractor
def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split(' ')
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

poem = '''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!'''

poem2 = '''Oh! Shall I tell you, Mama,
What's causing my annoyance?
Daddy wants me to reason
Like an adult,
But I say that sweets,
Are worth more than reason!'''

poem3 = '''Hush, little baby, don't say a word,
Mama's gonna buy you a mockingbird.
If that mockingbird don't sing,
Mama's gonna buy you a diamond ring.
If that diamond ring turns brass,
Mama's gonna buy you a looking glass.'''

print('------------------------\n')
print(pin_extractor([poem, poem2, poem3]))
print('------------------------\n')