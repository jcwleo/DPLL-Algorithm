from itertools import combinations
import random
import sys


def create_CNF(k, m, n, output):
    symbol_list = []
    for i in range(26):
        symbol_list.append(chr(i + 65))

    for i in range(26):
        symbol_list.append(chr(i + 97))

    symbol = symbol_list[:n]

    for i in range(len(symbol)):
        symbol.append('!' + symbol[i])

    clause_comb_symbol = list(combinations(list(combinations(symbol, k)), m))

    CNF = clause_comb_symbol[random.randint(0, len(clause_comb_symbol) - 1)]
    for i in CNF:
        print(' '.join(i).strip(' '))
        output.write(' '.join(i).strip(' '))
        if i != CNF[len(CNF) - 1]:
            output.write('\n')


def main():
    output = open('sampleCNF/output.txt', 'w')
    create_CNF(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), output)


if __name__ == '__main__':
    main()
