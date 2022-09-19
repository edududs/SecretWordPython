def upper(word):
    upperword = ''
    for letter in word:
        if letter.islower():
            letter = letter.upper()
            upperword += letter
        else:
            upperword += letter

    return upperword


def lower(word):
    lowerword = ''
    for letter in word:
        if letter.isupper():
            letter = letter.lower()
            lowerword += letter
        else:
            lowerword += letter

    return lowerword
