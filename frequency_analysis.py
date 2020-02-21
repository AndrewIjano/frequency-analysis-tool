import re
from argparse import ArgumentParser, FileType
import frequency_plot as freqplot

BASE = ord('A')

def format_text(text):
    return re.sub(r'[^a-zA-z]', '', text).upper()

def count_frequencies(text):
    formated_text = format_text(text)

    one_letter = {chr(BASE + i) : 0 for i in range(26)}
    digraphs   = {}
    trigraphs  = {}
    doubles    = {}

    N = len(formated_text) - 1

    for i in range(N):
        char = formated_text[i]

        if i > 0:
            digraph = prev_char + char
            if char == prev_char:
                doubles[digraph] = doubles.setdefault(digraph, 0) + 1

            digraphs[digraph] = digraphs.setdefault(digraph, 0) + 1

            if i < N - 1:
                next_char = formated_text[i+1]
                trigraph = digraph + next_char
                trigraphs[trigraph] = trigraphs.setdefault(trigraph, 0) + 1

        one_letter[char] = one_letter.setdefault(char, 0) + 1
        prev_char = char
    
    one_letter = {k: one_letter[k]/(N-1) for k in one_letter.keys()}

    return one_letter, digraphs, trigraphs, doubles


def analyse(document, is_ploting, LIST_SIZE=7):
    one_letter, digraphs, trigraphs, doubles = count_frequencies(document)

    if is_ploting:
        print('One letter frequency plot:')
        freqplot.plot(one_letter)

    def sorted_keys(d): return [
        k for k in sorted(d, key=d.get, reverse=True)]
    print('Frequencies:')
    print('one_letter:', ' '.join(sorted_keys(one_letter)[:LIST_SIZE]))
    print('digraphs:',   ' '.join(sorted_keys(digraphs)[:LIST_SIZE]))
    print('trigraphs:',  ' '.join(sorted_keys(trigraphs)[:LIST_SIZE]))
    print('doubles:',    ' '.join(sorted_keys(doubles)[:LIST_SIZE]))

if __name__ == '__main__':
    parser = ArgumentParser(
        prog='frequency_analysis.py',
        epilog='''
            Examples:\n
            python3 frequency_analysis.py textfile.txt -p
            ''')
    try:
        parser.add_argument(
            'textfile', metavar='textfile', nargs=1, help='the input textfile to be analysed', type=FileType('r'))
        parser.add_argument(
            '-p', nargs='?', dest='is_ploting', help='plots the frequency analysis graph', 
            const=True, default=False)
        args = parser.parse_args()
        analyse(args.textfile[0].read(), args.is_ploting)
    except:
        print()
        parser.print_help()
