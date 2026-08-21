def breakingRecords(scores):
    highest = scores[0]
    lowest = scores[0]
    high_breaking = 0
    low_breaking = 0

    for score in scores:
        if score > highest:
            high_breaking += 1
            highest = score
        elif score < lowest:
            low_breaking += 1
            lowest = score

    return high_breaking, low_breaking
