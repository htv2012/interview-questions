def superDigit(s: str, k: int) -> int:
    if k == 9:
        return 9

    s = str(s)
    sup = 0
    for digit in s:
        sup += int(digit)
        if sup > 9:
            sup -= 9

    if k == 1:
        return sup
    return superDigit(sup * k, 1)
