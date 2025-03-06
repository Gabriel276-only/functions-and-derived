import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import os

# Função para definir a função e sua derivada
def define_function():
    print("Digite a função f(x) usando a sintaxe do Python (use 'x' como variável):")
    print("Exemplo: x**3 + 2*x**2 - 5*x + 7")
    f_expr = input("f(x) = ")
    f = lambda x: eval(f_expr)
    
    print("\nDigite a derivada f'(x) usando a sintaxe do Python:")
    print("Exemplo: 3*x**2 + 4*x - 5")
    df_expr = input("f'(x) = ")
    df = lambda x: eval(df_expr)
    
    return f, df

# Função para encontrar pontos críticos
def find_critical_points(df):
    print("\nDigite os chutes iniciais para encontrar os pontos críticos (separados por espaço):")
    print("Exemplo: -3 0 3")
    guesses = list(map(float, input().split()))
    return fsolve(df, guesses)

# Função para plotar a função e sua derivada
def plot_function_and_derivative(ax, x, f, df, critical_points, plot_derivative=True):
    y = f(x)
    dy = df(x)
    
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.plot(x, y, label=r'$f(x)$', color='blue')
    
    if plot_derivative:
        ax.plot(x, dy, label=r"$f'(x)$", color='red', linestyle='dashed')
    
    # Marcar pontos críticos
    for cp in critical_points:
        if min(x) <= cp <= max(x):  # Apenas se estiver no intervalo
            ax.scatter(cp, f(cp), color='green', zorder=3, label=f'Crítico ({cp:.2f}, {f(cp):.2f})')

# Função para plotar a reta tangente
def plot_tangent_line(ax, x0, f, df):
    y0 = f(x0)
    dy0 = df(x0)
    tangent_x = np.linspace(x0 - 1, x0 + 1, 100)
    tangent_y = dy0 * (tangent_x - x0) + y0
    ax.plot(tangent_x, tangent_y, color='purple', linestyle='dotted', label=f'Tangente em x0={x0}')
    ax.scatter(x0, y0, color='blue', zorder=3)
    ax.text(x0, y0, f'  f({x0})', fontsize=12, verticalalignment='bottom', color='blue')

# Função principal
def main():
    print("Bem-vindo ao Gerador de Gráficos de Funções e Derivadas!")
    print("Este programa pode ser usado para análise matemática em diversas áreas.\n")
    
    # Definir a função e sua derivada
    f, df = define_function()
    
    # Encontrar pontos críticos
    critical_points = find_critical_points(df)
    print("\nPontos críticos encontrados:", critical_points)
    
    # Criar intervalo de valores de x
    x_min = float(input("\nDigite o valor mínimo de x: "))
    x_max = float(input("Digite o valor máximo de x: "))
    x = np.linspace(x_min, x_max, 400)
    
    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Escolher o que plotar
    plot_derivative = input("\nDeseja plotar a derivada? (s/n): ").strip().lower() == 's'
    plot_tangent = input("Deseja plotar a reta tangente? (s/n): ").strip().lower() == 's'
    
    plot_function_and_derivative(ax, x, f, df, critical_points, plot_derivative)
    
    if plot_tangent:
        while True:
            try:
                x0 = float(input("\nDigite um valor para x0 (entre {} e {}): ".format(x_min, x_max)))
                if x_min <= x0 <= x_max:
                    break
                else:
                    print("Valor fora do intervalo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Tente novamente.")
        plot_tangent_line(ax, x0, f, df)
    
    # Configurações finais do gráfico
    ax.legend()
    ax.grid()
    ax.set_title('Função e sua Derivada')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # Exportação do gráfico
    save_option = input("\nDeseja salvar o gráfico? (png/pdf/não): ").strip().lower()
    if save_option in ['png', 'pdf']:
        directory = input("Digite o diretório onde deseja salvar o gráfico (deixe em branco para o diretório atual): ").strip()
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        filename = os.path.join(directory, f'grafico.{save_option}')
        plt.savefig(filename, dpi=300 if save_option == 'png' else None)
        print(f"Gráfico salvo como '{filename}'")
    
    plt.show()

if __name__ == "__main__":
    main()