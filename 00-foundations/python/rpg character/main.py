def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string.'
    if name == '':
        return 'The character should have a name.'
    if len(name) > 10:
        return 'The character name is too long.'
    if ' ' in name:
        return 'The character name should not contain spaces.'
    if not all(isinstance(x, int) for x in (strength, intelligence, charisma)):
        return 'All stats should be integers'
    if not all(1 <= x <= 4 for x in (strength, intelligence, charisma)):
        return 'All stats should be 1 to 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

    def bar(value):
        return "●" * value + "○" * (10 - value)

    return (
        f'{name}\n'
        f'STR {bar(strength)}\n'
        f'INT {bar(intelligence)}\n'
        f'CHA {bar(charisma)}'
    )
