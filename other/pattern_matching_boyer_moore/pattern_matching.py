def match(src, pat):
    if pat == "":
        raise ValueError()

    pat_len = len(pat)
    table = {}
    for index, ch in enumerate(pat):
        table[ch] = pat_len - index - 1
    del table[ch]

    src_len = len(src)
    first = 0
    last = first + pat_len - 1

    while last < src_len:
        for index in range(pat_len - 1, -1, -1):
            if src[first + index] != pat[index]:
                first += table.get(src[last], pat_len)
                last = first + pat_len - 1
                break
        else:
            return first

    raise ValueError()
