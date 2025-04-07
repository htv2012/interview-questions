import string


def translate(inchar: str, k: int):
    if inchar in string.ascii_lowercase:
        band = string.ascii_lowercase
    elif inchar in string.ascii_uppercase:
        band = string.ascii_uppercase
    else:
        return inchar

    return band[(band.index(inchar) + k) % len(band)]


def caesarCipher(s, k):
    return "".join(translate(c, k) for c in s)
