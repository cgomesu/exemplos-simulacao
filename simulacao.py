from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import math

class Simulacao(ABC):
    def __init__(self, observacoes, seed):
        self.observacoes = observacoes
        self.seed = seed
        self.x = np.zeros(self.observacoes)
    
    @property
    def observacoes(self):
        return self.__observacoes
    @observacoes.setter
    def observacoes(self, observacoes:int):
        self.__observacoes = observacoes

    @property
    def seed(self):
        return self.__seed
    @seed.setter
    def seed(self, seed:int):
        self.__seed = seed

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x:np.ndarray):
        self.__x = x

    @abstractmethod
    def simulacao(self):
        pass

    def histograma(self, bins="auto"):
        # metodo bagual
        plt.hist(self.x, bins=bins)
        plt.show()

class Binomial(Simulacao):
    def __init__(self, observacoes:int, seed:int, n:int, theta:float):
        super().__init__(observacoes, seed)
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

    def simulacao(self):
        np.random.seed(self.seed)
        for i in range(len(self.x)):
            uniform = np.random.uniform(low=0, high=1, size=self.n)
            # soma elementos de uma array booleana condicao etapa 2
            self.x[i] = (uniform <= self.theta).sum()


class Triangular(Simulacao):
    def __init__(self, observacoes:int, seed:int, a:float, b:float, c:float):
        super().__init__(observacoes, seed)
        self.a = a
        self.b = b
        self.c = c
    
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, a:float):
        self.__a = a
    
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, b:float):
        self.__b = b
        
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, c:float):
        self.__c = c

    def __cdf(self, valor):
        if valor <= self.a:
            return 0
        elif self.a < valor <= self.c:
            return math.pow(valor-self.a, 2)/((self.b-self.a)*(self.c-self.a))
        elif self.c < valor < self.b:
            return 1 - math.pow(self.b-valor, 2)/((self.b-self.a)*(self.b-self.c))
        else:
            return 1

    def __inv_cdf(self, valor:float):
        if valor == 0:
            return self.a
        elif 0 < valor < self.__cdf(self.c):
            return self.a + math.sqrt(valor*(self.c-self.a)*(self.b-self.a))
        elif self.__cdf(self.c) <= valor < 1:
            return self.b - math.sqrt((1-valor)*(self.b-self.a)*(self.b-self.c))
        elif valor == 1:
            return self.b
        else:
            raise ValueError(f"O valor '{valor}' não está no intervalo de probabilidade.")
    
    def simulacao(self, metodo="inversa"):
        if metodo == "inversa":
            return self.__simulacao_inversa()
        raise ValueError(f"O método {metodo} é inválido.")
    
    def __simulacao_inversa(self):
        np.random.seed(self.seed)
        uniform = np.random.uniform(low=0, high=1, size=self.observacoes)
        inv_tri = np.vectorize(self.__inv_cdf)
        self.x = inv_tri(uniform)