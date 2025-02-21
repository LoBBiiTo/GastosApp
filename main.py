import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Configurar plt style
plt.style.use('dark_background')

def agregar_gasto():
    categoria = entrada_categoria.get()
    monto = float(entrada_monto.get())
    gastos[categoria] = gastos.get(categoria, 0) + monto
    entrada_categoria.delete(0, tk.END)
    entrada_monto.delete(0, tk.END)

def mostrar_grafica():
    categorias = list(gastos.keys())
    montos = list(gastos.values())
    plt.figure(facecolor='#2C3E50')
    ax = plt.gca()
    ax.set_facecolor('#2c3e50')
    bars = plt.bar(categorias, montos, color='#3498db')

    # Agregar valor a los labels encima de las barras
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height,
                 f'${int(height)}', ha='center', va='bottom', color='white')

    plt.title("Gastos", color='white', pad=20)
    plt.xticks(color='white')
    plt.yticks(color='white')
    plt.show()

gastos = {}

# Crear la ventana principal
root = tk.Tk()
root.title("Rastreador de Gastos")
root.configure(bg='#2c3e50')
root.geometry("400x500")
root.resizable(False, False)

style = ttk.Style()
style.configure('TFrame', background='#2c3e50')
style.configure('TLabel', background='#2c3e50', foreground='white', font=('Montserrat', 14))
style.configure('TEntry', padding=5)
style.configure('TButton', padding=10, font=('Montserrat', 12))

# Contenedor principal
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Título
titulo = ttk.Label(main_frame, text="Lista de gastos", font=('Montserrat', 14, 'bold'))
titulo.pack(pady=(0, 20))

# Input frame
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=10)

# Categoría
cat_frame = ttk.Frame(input_frame)
cat_frame.pack(fill=tk.X, pady=5)
ttk.Label(cat_frame, text="Categoria:").pack(anchor=tk.W)
entrada_categoria = ttk.Entry(cat_frame, font=('Montserrat', 12))
entrada_categoria.pack(fill=tk.X, pady=(5, 0))

# Monto
monto_frame = ttk.Frame(input_frame)
monto_frame.pack(fill=tk.X, pady=5)
ttk.Label(monto_frame, text="Monto:").pack(anchor=tk.W)
entrada_monto = ttk.Entry(monto_frame, font=('Montserrat', 12))
entrada_monto.pack(fill=tk.X, pady=(5, 0))

# Botones Frame
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=(20, 0))

agregar_btn = tk.Button(button_frame, text="Agregar Gasto", command=agregar_gasto,
                        bg='#27ae60', fg='white', font=('Montserrat', 12, 'bold'),
                        relief=tk.FLAT, padx=20, pady=10)
agregar_btn.pack(fill=tk.X, pady=5)

grafica_btn = tk.Button(button_frame, text="Mostrar Grafica", command=mostrar_grafica,
                        bg='#3498db', fg='white', font=('Montserrat', 12, 'bold'),
                        relief=tk.FLAT, padx=20, pady=10)
grafica_btn.pack(fill=tk.X, pady=5)

root.mainloop()