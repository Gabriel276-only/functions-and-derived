# Visualizador de Funções e Derivadas

## Descrição

Este projeto gera um gráfico de uma função matemática e sua derivada, permitindo ao usuário escolher um valor para visualizar pontos específicos.

## Funcionalidades

- Exibe o gráfico de uma função polinomial e sua derivada.

- Permite ao usuário inserir um valor para visualizar os pontos da função e da derivada.

## Gráfico gerado utilizando a biblioteca matplotlib 

- **Tecnologias Utilizadas**

- **Python 3**

- **NumPy**

- **Matplotlib**

### Como Executar

- **Certifique-se de ter o Python instalado.**

- **Instale as dependências necessárias:**

```bash
pip install numpy matplotlib
```

### Execute o script:

```bash
python nome_do_arquivo.py
```

- **Insira um valor para x0 quando solicitado.**


### Exemplo de Código

---
```
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 2*x**2 - 5*x + 7

def df(x):
    return 3*x**2 + 4*x - 5
---
x = np.linspace(-5, 5, 400)
y = f(x)
dy = df(x)
---
x0 = float(input("Digite um valor para x0: "))

plt.figure(figsize=(8, 6))
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.plot(x, y, label='f(x)', color='blue')
plt.plot(x, dy, label="f'(x)", color='red', linestyle='dashed')
plt.scatter(x0, f(x0), color='blue')
plt.scatter(x0, df(x0), color='red')
plt.legend()
plt.grid()
plt.show()
```
---
### Melhorias Futuras

- **Implementar uma interface gráfica interativa.**

- **Permitir entrada de diferentes funções definidas pelo usuário.**



