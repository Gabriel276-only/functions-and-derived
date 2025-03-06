import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import os
from sympy import symbols, diff, lambdify, sympify

# Definir a função de entrada segura
def define_function():
    x = symbols('x')
    
    while True:
        try:
            f_expr = sympify(input("Digite a função f(x): "))
            df_expr = diff(f_expr, x)
            f = lambdify(x, f_expr, 'numpy')
            df = lambdify(x, df_expr, 'numpy')
            print(f"Derivada calculada automaticamente: f'(x) = {df_expr}")
            return f, df, x
        except Exception as e:
            print(f"Erro na entrada: {e}. Certifique-se de usar a sintaxe correta (ex: 'exp(x)', 'log(x)', 'sin(x)', etc.). Tente novamente.")

# Encontrar pontos críticos automaticamente
def find_critical_points(df, x_min, x_max):
    x_values = np.linspace(x_min, x_max, 1000)
    
    # Verifica se df é uma função numérica
    if not callable(df):
        raise TypeError("A derivada 'df' não é uma função numérica.")
    
    df_values = df(x_values)  # Avalia a derivada nos pontos x_values
    
    # Encontrar onde a derivada muda de sinal
    critical_points = []
    for i in range(len(x_values) - 1):
        if df_values[i] * df_values[i + 1] < 0:
            root = fsolve(df, (x_values[i] + x_values[i + 1]) / 2)  # Chute inicial no meio do intervalo
            critical_points.append(root[0])
    
    # Remover duplicatas e arredondar
    critical_points = np.unique(np.round(critical_points, decimals=5))
    return critical_points

# Função para plotar gráficos
def plot_function_and_derivative(ax, x, f, df, critical_points, plot_derivative=True):
    y = f(x)
    dy = df(x)
    
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.plot(x, y, label=r'$f(x)$', color='blue')
    
    if plot_derivative:
        ax.plot(x, dy, label=r"$f'(x)$", color='red', linestyle='dashed')
    
    for cp in critical_points:
        if min(x) <= cp <= max(x):
            ax.scatter(cp, f(cp), color='green', zorder=3, label=f'Crítico ({cp:.2f}, {f(cp):.2f})')

# Função principal
def main():
    print("Bem-vindo ao Gerador de Gráficos de Funções e Derivadas!\n")
    
    f, df, x_sym = define_function()
    
    while True:
        try:
            x_min = float(input("\nDigite o valor mínimo de x: "))
            x_max = float(input("Digite o valor máximo de x: "))
            if x_min < x_max:
                break
            print("x_min deve ser menor que x_max. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")
    
    critical_points = find_critical_points(df, x_min, x_max)
    print("\nPontos críticos encontrados:", critical_points)
    
    x = np.linspace(x_min, x_max, 400)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    plot_derivative = input("\nDeseja plotar a derivada? (s/n): ").strip().lower() == 's'
    plot_function_and_derivative(ax, x, f, df, critical_points, plot_derivative)
    
    ax.legend()
    ax.grid()
    ax.set_title('Função e sua Derivada')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
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