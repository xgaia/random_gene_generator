#! /usr/bin/python3

import sys
import getopt
import random
from random import randint
def usage():

    print('Usage:')
    print('\t./random_genes_generator.py -n <lines>\n')
    print('<lines>: number of lines in the output file\n')
    print('optional args:\n')
    print('\t-o, --output-file : name of the result files (default : random_genes.csv)')

def get_args(argv):

    output = 'random_genes.csv'
    res = {}
    
    try:
        opts, argvs = getopt.getopt(argv, 'hn:o:', ['lines=', 'output-file='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    if not opts:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit(2)
        elif opt in ('-n', '--lines'):
            lines_number = int(arg)
        elif opt in ('-o', '--output-file'):
            output = str(arg)

    if not lines_number:
        print('/!\ -n arg is mandatory !\n\n')
        usage()
        sys.exit(2)

    res['lines_number'] = lines_number
    res['output'] = output

    return res

def generate_file(lines_number, of):

    fp = open(of,'w')
    fp.write('gene\tstart\tend\tref\ttaxon\n')
    tax_list = ['bla', 'bli', 'blo', 'blu']

    for x in range(0, lines_number):
        start = randint(0,10000000)
        end = randint(int(start),10000000)
        ref = 'G' + str(randint(1,5))
        taxon = random.choice(tax_list)
        gene = 'gene' + str(x)
        fp.write(gene + '\t' + str(start) + '\t' + str(end) + '\t' + ref + '\t' + taxon + '\n')


def main():
    args = get_args(sys.argv[1:])

    ln = args.get('lines_number')
    of = args.get('output')

    generate_file(ln, of)

if __name__ == "__main__":
    main()
