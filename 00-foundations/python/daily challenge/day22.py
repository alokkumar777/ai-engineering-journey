def get_average_grade(scores):
    total = round(sum(scores) / len(scores))

    if total >= 97 and total <= 100:
        return "A+"
    if total >= 93 and total <= 96:
        return "A"
    if total >= 90 and total <= 92:
        return "A-"
    if total >= 87 and total <= 89:
        return "B+"
    if total >= 83 and total <= 86:
        return "B"
    if total >= 80 and total <= 82:
        return "B-"
    if total >= 77 and total <= 79:
        return "C+"
    if total >= 73 and total <= 76:
        return "C"
    if total >= 70 and total <= 72:
        return "C-"
    if total >= 67 and total <= 69:
        return "D+"
    if total >= 63 and total <= 66:
        return "D"
    if total >= 60 and total <= 62:
        return "D-"
    if total < 60:
        return "F"

print(get_average_grade([92, 91, 90, 94, 89, 93]))
print(get_average_grade([84, 89, 85, 100, 91, 88, 79]))
print(get_average_grade([63, 69, 65, 66, 71, 64, 65]))
print(get_average_grade([97, 98, 99, 100, 96, 97, 98, 99, 100]))
print(get_average_grade([75, 100, 88, 79, 80, 78, 64, 60]))
print(get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59]))