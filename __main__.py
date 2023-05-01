#!/usr/bin/env python3
from simulacao import Binomial

def main():
    m = 1000
    seed = 6548
    n = 10
    theta = .5
    binomial = Binomial(m, seed, n, theta)
    binomial.simulacao(234)
    binomial.histograma()

if __name__ == '__main__':
    main()