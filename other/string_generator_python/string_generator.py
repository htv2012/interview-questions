def string_generator(mystr):
    question_mark_count = mystr.count('?')
    possibilities = pow(2, question_mark_count)
    for i in range(possibilities):
        replacement = '{0:0{w}b}'.format(i, w=question_mark_count)
        it = iter(replacement)
        yield ''.join(c if c != '?' else next(it) for c in mystr)

def main():
    mystr = 'a?b?c?'
    for s in string_generator(mystr):
        print s

if __name__ == '__main__':
    main()
