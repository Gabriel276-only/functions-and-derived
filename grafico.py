import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import os
from sympy import symbols, diff, lambdify, sympify
import tkinter as tk
from tkinter import messagebox, simpledialog

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
            print(f"Erro: {e}. Use sintaxe correta (ex: 'exp(x)', 'log(x)', 'sin(x)').")

def find_critical_points(df, x_min, x_max):
    x_values = np.linspace(x_min, x_max, 1000)
    
    try:
        df_values = df(x_values)
        if not isinstance(df_values, np.ndarray):
            raise TypeError("df(x) deve retornar um array NumPy.")
    except Exception as e:
        print(f"Erro ao avaliar a derivada: {e}")
        return []

    critical_points = []
    for i in range(len(x_values) - 1):
        if df_values[i] * df_values[i + 1] < 0:
            try:
                root = fsolve(df, (x_values[i] + x_values[i + 1]) / 2)
                if x_min <= root[0] <= x_max:
                    critical_points.append(root[0])
            except Exception as e:
                print(f"Erro ao encontrar ponto crítico: {e}")
    
    return np.unique(np.round(critical_points, 5))

def plot_function_and_derivative(ax, x, f, df, critical_points, plot_derivative=True):
    try:
        y = f(x)
        dy = df(x)
    except Exception as e:
        print(f"Erro ao calcular valores de f(x): {e}")
        return
    
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.plot(x, y, label=r'$f(x)$', color='blue')
    
    if plot_derivative:
        ax.plot(x, dy, label=r"$f'(x)$", color='red', linestyle='dashed')
    
    for cp in critical_points:
        try:
            ax.scatter(cp, f(cp), color='green', zorder=3, label=f'Crítico ({cp:.2f}, {f(cp):.2f})')
        except Exception:
            pass

def main():
    print("Bem-vindo ao Gerador de Gráficos de Funções e Derivadas!\n")
    
    f, df, x_sym = define_function()
    
    while True:
        try:
            x_min = float(input("\nDigite o valor mínimo de x: "))
            x_max = float(input("Digite o valor máximo de x: "))
            if x_min < x_max:
                break
            print("x_min deve ser menor que x_max.")
        except ValueError:
            print("Entrada inválida.")

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
        directory = input("Diretório para salvar (vazio para atual): ").strip()
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        filename = os.path.join(directory or ".", f'grafico.{save_option}')
        plt.savefig(filename, dpi=300 if save_option == 'png' else None)
        print(f"Gráfico salvo em '{filename}'")
    
    plt.show()

def gui_main():
    root = tk.Tk()
    root.title("Gerador de Gráficos de Funções e Derivadas")
    
    def on_submit():
        try:
            f_expr = sympify(entry_function.get())
            x = symbols('x')
            df_expr = diff(f_expr, x)
            f = lambdify(x, f_expr, 'numpy')
            df = lambdify(x, df_expr, 'numpy')
            
            x_min = float(entry_xmin.get())
            x_max = float(entry_xmax.get())
            
            if x_min >= x_max:
                messagebox.showerror("Erro", "x_min deve ser menor que x_max.")
                return
            
            critical_points = find_critical_points(df, x_min, x_max)
            x_values = np.linspace(x_min, x_max, 400)
            
            fig, ax = plt.subplots(figsize=(8, 6))
            plot_derivative = plot_derivative_var.get()
            plot_function_and_derivative(ax, x_values, f, df, critical_points, plot_derivative)
            
            ax.legend()
            ax.grid()
            ax.set_title('Função e sua Derivada')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            
            save_option = save_option_var.get()
            if save_option in ['png', 'pdf']:
                directory = entry_directory.get()
                if directory and not os.path.exists(directory):
                    os.makedirs(directory)
                filename = os.path.join(directory or ".", f'grafico.{save_option}')
                plt.savefig(filename, dpi=300 if save_option == 'png' else None)
                messagebox.showinfo("Sucesso", f"Gráfico salvo em '{filename}'")
            
            plt.show()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    tk.Label(root, text="Função f(x):").grid(row=0, column=0, padx=10, pady=10)
    entry_function = tk.Entry(root, width=30)
    entry_function.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(root, text="x mínimo:").grid(row=1, column=0, padx=10, pady=10)
    entry_xmin = tk.Entry(root, width=10)
    entry_xmin.grid(row=1, column=1, padx=10, pady=10)
    
    tk.Label(root, text="x máximo:").grid(row=2, column=0, padx=10, pady=10)
    entry_xmax = tk.Entry(root, width=10)
    entry_xmax.grid(row=2, column=1, padx=10, pady=10)
    
    plot_derivative_var = tk.BooleanVar(value=True)
    tk.Checkbutton(root, text="Plotar derivada", variable=plot_derivative_var).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    save_option_var = tk.StringVar(value="não")
    tk.Label(root, text="Salvar gráfico como:").grid(row=4, column=0, padx=10, pady=10)
    tk.Radiobutton(root, text="PNG", variable=save_option_var, value="png").grid(row=4, column=1, padx=10, pady=10)
    tk.Radiobutton(root, text="PDF", variable=save_option_var, value="pdf").grid(row=5, column=1, padx=10, pady=10)
    tk.Radiobutton(root, text="Não salvar", variable=save_option_var, value="não").grid(row=6, column=1, padx=10, pady=10)
    
    tk.Label(root, text="Diretório para salvar:").grid(row=7, column=0, padx=10, pady=10)
    entry_directory = tk.Entry(root, width=30)
    entry_directory.grid(row=7, column=1, padx=10, pady=10)
    
    tk.Button(root, text="Gerar Gráfico", command=on_submit).grid(row=8, column=0, columnspan=2, padx=10, pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    gui_main()