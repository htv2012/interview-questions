import collections

sample = "  cabbac mom dad sister   mom sonos daughter mom deed a bb dad  bar"
counter = collections.OrderedDict()
left = 0
sample_length = len(sample)
while left < sample_length:
    # Skip white spaces to the start of a word
    while sample[left] == ' ':
        left += 1
    
    # Skip to the end of a word
    right = left
    while right < sample_length and sample[right] != ' ':
        right += 1
    word = sample[left:right]
    right -= 1

    # Palindromic test
    anchor = right
    while left < right:
        if sample[left] != sample[right]: break
        left += 1
        right -= 1
    else:
        counter.setdefault(word, 0)
        counter[word] += 1
    left = anchor + 1

for w in counter:
    print '{} {} time{}'.format(w, counter[w], 's' if counter[w] > 1 else '')