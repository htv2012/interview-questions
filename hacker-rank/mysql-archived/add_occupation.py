import csv
import pathlib
import fileinput
import random

choices = "Admin Doctor Nurse Support".split()
original = pathlib.Path('occupation.csv')
bak = original.with_suffix('.bak')
bak.write_text(original.read_text())

with open(original, 'w') as ostream, open(bak, 'r') as istream:
    reader = csv.DictReader(istream)
    writer = csv.DictWriter(ostream, fieldnames=reader.fieldnames + ['occupation'])
    for row in reader:
        row['occupation'] = random.choice(choices)
        writer.writerow(row)

