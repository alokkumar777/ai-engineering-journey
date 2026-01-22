def to_consonant_case(s):
    result = []

    for ch in s:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                result.append(ch.lower())
            else:
                result.append(ch.upper())
        else:
            result.append(ch)

    return ''.join(result).replace('-', '_')



print(to_consonant_case("helloworld"))
print(to_consonant_case("HELLOWORLD"))
print(to_consonant_case("_hElLO-WOrlD-"))