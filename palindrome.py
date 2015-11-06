import sys
from math import ceil

checker = lambda x: x[:len(x)//2:] == x[:int(ceil(len(x)/2)-1):-1]

if '__main__' == __name__:
    print(checker(sys.argv[1]))
