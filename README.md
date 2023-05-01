# Simulacao - Monte Carlo - Transformacao Inversa

Programa Python de simulação via método de Monte Carlo usando transformações inversas.

## Funcao Triangular

Para os parâmetros $a, b, c$ que indicam, respectivamente, o limite inferior, moda e limite superior de uma distribuição triangular, temos que a probabilidade de uma v.a.c. $X$ é dada pela seguinte função densidade de probabilidade

$f(x) = \begin{cases}
    \frac{2(x-a)}{(b-a)(c-a)} & \text{se }a\le x\lt c \\
    \frac{2}{b-a} &\text{se }x=c \\
    \frac{2(b-x)}{(b-a)(b-c)} &\text{se }c\lt x \le b \\
    0 &\text{restante}
    \end{cases}$

e função densidade acumulada de probabilidade

$F(x) = \begin{cases}
    0 &\text{se }x\le a \\
    \frac{(x-a)^2}{(b-a)(c-a)} &\text{se }a\lt x \le c\\
    1-\frac{(b-x)^2}{(b-a)(b-c)} &\text{se } c\lt x\lt b\\
    1 &\text{se }b\le x
    \end{cases}$

e cuja inversa será

$F^{-1}(u) = \begin{cases}
    a+\sqrt{u(c-a)(b-a)} &\text{se }0\lt u \lt F(c)\\
    b-\sqrt{(1-u)(b-a)(b-c)} &\text{se } F(c)\le u\lt 1
    \end{cases}$

[top](#simulacao---monte-carlo---transformacao-inversa)
