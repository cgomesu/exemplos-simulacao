#!/usr/bin/env python3
from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt

class Simulacao(ABC):
    def __init__(self, observacoes):
        self.observacoes = observacoes
        self.x = np.zeros(self.observacoes)
    
    @property
    def observacoes(self):
        return self.__observacoes
    @observacoes.setter
    def observacoes(self, observacoes:int):
        self.__observacoes = observacoes
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x:np.ndarray):
        self.__x = x
    
    @abstractmethod
    def simulacao(self):
        pass

    @abstractmethod
    def histograma(self):
        pass

class Binomial(Simulacao):
    def __init__(self, observacoes:int, n:int, theta:float):
        super().__init__(observacoes)
        self.n = n
        self.theta = theta
    
    @property
    def n(self):
        return self.__n
    @n.setter
    def n(self, n:int):
        self.__n = n
    @property
    def theta(self):
        return self.__theta
    @theta.setter
    def theta(self, theta:float):
        self.__theta = theta

    def simulacao(self, seed):
        np.random.seed(seed)
        for i in range(len(self.x)):
            uniform = np.random.uniform(low=0, high=1, size=self.n)
            # soma elementos de uma array booleana condicao etapa 2
            self.x[i] = (uniform <= self.theta).sum()

    def histograma(self, bins="auto"):
        plt.hist(self.x, bins=bins)
        plt.show()