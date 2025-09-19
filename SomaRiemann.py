import math
from typing import Callable


def Integrando(f: Callable[[float], float], a: float, b: float, n: int)-> float:
    
    if n <= 0:
        raise ValueError("É PRECISO QUE N > 0")
    if a == b:
        return 0.0 #não há área
    if b < a:
        raise ValueError("É PRECISO QUE B > A")
    
    dx = (b - a)/ n #representa os intervalos
    somas = 0.0

    for i in range (n):
        x = a + (i + 0.5) * dx #ponto médio
        y = f(x)
        somas += y
    return somas * dx


#O código é basicamente isso, só restam os casos testes

########################################################################################################################


if __name__ == "__main__":
    # Exemplo 1: ∫_0^1 x^2 dx = 1/3 ≈ 0.333333...
    f1 = lambda x: x**2
    print("Exemplo 1: ∫_0^1 x^2 dx")
    print("  n=4   :", Integrando(f1, 0.0, 1.0, n=4))

    # Exemplo 2: ∫_0^π sin(x) dx = 2
    print("\nExemplo 2: ∫_0^π sin(x) dx")
    print("  n=1000:", Integrando(math.sin, 0.0, math.pi, n=1000))

    # Exemplo 3: ∫_1^e 1/x dx = 1
    f3 = lambda x: 1.0 / x
    print("\nExemplo 3: ∫_1^e 1/x dx")
    print("  n=2000:", Integrando(f3, 1.0, math.e, n=2000))
    # Exemplo 4: ∫_0^1 e^x dx = e - 1
    print("\nExemplo 4: ∫_0^1 e^x dx")
    print("  n=2000:", Integrando(math.exp, 0.0, 1.0, n=2000))

    # Exemplo 5: ∫_0^1 sqrt(x) dx = 2/3
    print("\nExemplo 5: ∫_0^1 sqrt(x) dx")
    print("  n=4000:", Integrando(math.sqrt, 0.0, 1.0, n=4000))

    # Exemplo 6: ∫_0^{π/2} (sin^2 x + cos^2 x) dx = π/2
    f6 = lambda x: math.sin(x)**2 + math.cos(x)**2
    print("\nExemplo 6: ∫_0^{π/2} (sin^2 x + cos^2 x) dx")
    print("  n=3000:", Integrando(f6, 0.0, math.pi/2, n=3000))

    # Exemplo 7: ∫_0^1 1/(1+x^2) dx = arctan(1) - arctan(0) = π/4
    f7 = lambda x: 1.0 / (1.0 + x*x)
    print("\nExemplo 7: ∫_0^1 1/(1+x^2) dx")
    print("  n=5000:", Integrando(f7, 0.0, 1.0, n=5000))

    # Exemplo 8: ∫_0^1 x^3 dx = 1/4
    f8 = lambda x: x**3
    print("\nExemplo 8: ∫_0^1 x^3 dx")
    print("  n=2000:", Integrando(f8, 0.0, 1.0, n=2000))

    # Exemplo 9: ∫_0^π cos(x) dx = 0
    print("\nExemplo 9: ∫_0^π cos(x) dx")
    print("  n=2000:", Integrando(math.cos, 0.0, math.pi, n=2000))

    # Exemplo 10: ∫_1^e log(x) dx = 1
    print("\nExemplo 10: ∫_1^e log(x) dx")
    print("  n=4000:", Integrando(math.log, 1.0, math.e, n=4000))
