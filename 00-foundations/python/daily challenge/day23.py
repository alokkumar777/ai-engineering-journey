# check valid hex code
import re
def is_valid_hex(s):
    pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    return bool(re.match(pattern, s))

print(is_valid_hex("#123"))
print(is_valid_hex("#123abc"))
print(is_valid_hex("#ABCDEF"))
print(is_valid_hex("#0a1B2c"))
print(is_valid_hex("#12G"))
print(is_valid_hex("#1234567"))
print(is_valid_hex("fff"))
