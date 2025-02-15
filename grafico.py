import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Função e sua derivada
def f(x):
    return x**3 + 2*x**2 - 5*x + 7

def df(x):
    return 3*x**2 + 4*x - 5

# Encontrar pontos críticos resolvendo f'(x) = 0
critical_points = fsolve(df, [-3, 0, 3])  # Chutes iniciais para encontrar raízes

# Criar intervalo de valores de x
x = np.linspace(-5, 5, 400)
y = f(x)
dy = df(x)

# Criar o gráfico
fig, ax = plt.subplots(figsize=(8, 6))
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Plotando a função original e sua derivada
ax.plot(x, y, label=r'$f(x) = x^3 + 2x^2 - 5x + 7$', color='blue')
ax.plot(x, dy, label=r"$f'(x) = 3x^2 + 4x - 5$", color='red', linestyle='dashed')

# Marcar pontos críticos
for cp in critical_points:
    if -5 <= cp <= 5:  # Apenas se estiver no intervalo
        ax.scatter(cp, f(cp), color='green', zorder=3, label=f'Crítico ({cp:.2f}, {f(cp):.2f})')

# Reta tangente em um ponto escolhido pelo usuário
x0 = float(input("Digite um valor para x0: "))
y0 = f(x0)
dy0 = df(x0)

# Equação da reta tangente: y = dy0 * (x - x0) + y0
tangent_x = np.linspace(x0 - 1, x0 + 1, 100)
tangent_y = dy0 * (tangent_x - x0) + y0
ax.plot(tangent_x, tangent_y, color='purple', linestyle='dotted', label=f'Tangente em x0={x0}')

# Destacando o ponto
ax.scatter(x0, y0, color='blue', zorder=3)
ax.scatter(x0, dy0, color='red', zorder=3)
ax.text(x0, y0, f'  f({x0})', fontsize=12, verticalalignment='bottom', color='blue')
ax.text(x0, dy0, f'  f({x0})', fontsize=12, verticalalignment='bottom', color='red')

ax.legend()
ax.grid()
ax.set_title('Função e sua Derivada')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Exportação do gráfico
save_option = input("Deseja salvar o gráfico? (png/pdf/não): ").strip().lower()
if save_option == 'png':
    plt.savefig('grafico.png', dpi=300)
    print("Gráfico salvo como 'grafico.png'")
elif save_option == 'pdf':
    plt.savefig('grafico.pdf')
    print("Gráfico salvo como 'grafico.pdf'")

plt.show()
