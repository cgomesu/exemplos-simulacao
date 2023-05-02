#!/usr/bin/env python3
from simulacao import Binomial
from simulacao import Triangular

def main():
    m = 10000
    seed = 123
    # n = 10
    # theta = .5
    # binomial = Binomial(m, seed, n, theta)
    # binomial.simulacao(234)
    # binomial.histograma()
    a = 0
    c = .6
    b = 1
    triangular = Triangular(m, seed, a, b, c)
    triangular.simulacao(metodo='inversa')
    triangular.histograma()

if __name__ == '__main__':
    main()