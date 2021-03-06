import sys
from math import ceil

def checker(x):
    x = x.upper()
    return x[:len(x)//2:] == x[:int(ceil(len(x)/2.0)-1):-1]

if '__main__' == __name__:
    try:
        print(checker(sys.argv[1]))
    except IndexError:
        sys.stderr.write("Requires one argument")
