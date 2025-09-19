# Integrando-com-Riemann
   Projeto em Python para resolver integrais utilizando a soma de Riemann.

# Como Funciona?

1. Pegamos um intervalo [a , b] e dividimos em "n" partes --> Cuja cada parte tem Delta X de largura, sendo Delta X = (b - a) / n.
2. Em cada parte "n", avaliamos a função pelo ponto médio: x = a + (i + 0.5) * dx
3. Somando as áreas de "n" retângulos, conseguimosn uma aproximação da área, e quanto maior o "n", a área será mais aproximada. Utilizamos a variável "somas" como o somatório, somando cada áres.
   
# Exemplos:

No final do arquivo há 10 exemplos, como:

1. Integração de \(x^2\) em \([0,1]\):
   
   $$\int_{0}^{1} x^{2}\,dx \;=\; \frac{1}{3} \;\approx\; 0.3333$$

2. Integração de \(\sin x\) em \([0,\pi]\):
   
   $$\int_{0}^{\pi} \sin x\,dx \;=\; 2$$

3. Integração de \(1/x\) em \([1,e]\):
   
   $$\int_{1}^{e} \frac{1}{x}\,dx \;=\; \ln(e)-\ln(1) \;=\; 1$$

4. Integração de \(e^{x}\) em \([0,1]\):
   
   $$\int_{0}^{1} e^{x}\,dx \;=\; e-1$$

5. Integração de \(\sqrt{x}\) em \([0,1]\):
   
   $$\int_{0}^{1} \sqrt{x}\,dx \;=\; \frac{2}{3} \;\approx\; 0.6667$$

6. Identidade trigonométrica em \([0,\tfrac{\pi}{2}]\):
   
   $$\int_{0}^{\pi/2} \big(\sin^{2}x+\cos^{2}x\big)\,dx \;=\; \int_{0}^{\pi/2} 1\,dx \;=\; \frac{\pi}{2}$$

7. Integração de \(\frac{1}{1+x^{2}}\) em \([0,1]\):
   
   $$\int_{0}^{1} \frac{1}{1+x^{2}}\,dx \;=\; \arctan(1) - \arctan(0) \;=\; \frac{\pi}{4} \;\approx\; 0.7854$$

8. Integração de \(x^{3}\) em \([0,1]\):
   
   $$\int_{0}^{1} x^{3}\,dx \;=\; \frac{1}{4} \;=\; 0.25$$

9. Integração de \(\cos x\) em \([0,\pi]\):
   
   $$\int_{0}^{\pi} \cos x\,dx \;=\; \sin x \Big|_{0}^{\pi} \;=\; 0$$

10. Integração de \(\ln x\) em \([1,e]\):
    
    $$\int_{1}^{e} \ln x\,dx \;=\; \big(x\ln x - x\big)\Big|_{1}^{e}
    \;=\; (e\cdot 1 - e) - (1\cdot 0 - 1) \;=\; 1$$

# Como utilizar o código?
1. Defina a função:
   f = lambda x: x*x.
2. Escolha o intervalo [a;b]
   b precisa ser maior que a.
3. Escolha a quantidade de repartições(n):
   n > 0
4. Função Integrando:
   print( Integrando(f, a, b, n))
5. Ilustrando:
∫_0^1 1/(1+x^2) dx = π/4
f = lambda x: 1.0 / (1.0 + x*x)
a = 0.0
b = 1.0
n = 5000
print("Integral ≈", Integrando(f, a, b, n))

# Autor
Ian da Silva Torquato - Discente do curso de Engenharia de Computação (Universidade Federal do Ceará)
# Vídeo Explicativo
https://youtu.be/MazpjRmd-uY
