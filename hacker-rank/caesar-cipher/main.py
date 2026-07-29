from string import ascii_lowercase, ascii_uppercase


def translate(inchar: str, k: int):
    for band in [ascii_lowercase, ascii_uppercase]:
        if inchar in band:
            index = (band.index(inchar) + k) % len(band)
            return band[index]
    return inchar


def caesarCipher(s, k):
    return "".join(translate(c, k) for c in s)
