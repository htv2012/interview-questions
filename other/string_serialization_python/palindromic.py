import collections

def is_palindomic(a_string):
    return str(a_string) == str(a_string)[::-1]

sample = "mom dad sister sonos daughter mom deed a bb dad  "
counter = collections.Counter(w for w in sample.split() if is_palindomic(w))
for w in sorted(counter):
    print '{} {} time{}'.format(w, counter[w], 's'[counter[w]==1:])
