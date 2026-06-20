import tkinter as tk
from tkinter import messagebox
from funciones import operar_numeros


class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Alegre")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Colores armonizados azul y naranja
        self.color_azul = "#4A90E2"
        self.color_azul_oscuro = "#357ABD"
        self.color_naranja = "#FF9F43"
        self.color_naranja_claro = "#FFB366"
        self.color_fondo = "#E8F4FD"
        self.color_blanco = "#FFFFFF"
        
        # Configurar fondo
        self.root.configure(bg=self.color_fondo)
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Título
        titulo = tk.Label(
            self.root,
            text="🧮 Calculadora Alegre",
            font=("Arial", 24, "bold"),
            bg=self.color_fondo,
            fg=self.color_azul_oscuro
        )
        titulo.pack(pady=20)
        
        # Marco para los números
        marco_numeros = tk.Frame(self.root, bg=self.color_fondo)
        marco_numeros.pack(pady=10)
        
        # Primer número
        tk.Label(
            marco_numeros,
            text="Primer número:",
            font=("Arial", 12),
            bg=self.color_fondo,
            fg=self.color_azul_oscuro
        ).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        
        self.entry_num1 = tk.Entry(
            marco_numeros,
            font=("Arial", 14),
            width=15,
            bg=self.color_blanco,
            fg=self.color_azul_oscuro,
            insertbackground=self.color_naranja
        )
        self.entry_num1.grid(row=0, column=1, padx=5, pady=5)
        
        # Segundo número
        tk.Label(
            marco_numeros,
            text="Segundo número:",
            font=("Arial", 12),
            bg=self.color_fondo,
            fg=self.color_azul_oscuro
        ).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        
        self.entry_num2 = tk.Entry(
            marco_numeros,
            font=("Arial", 14),
            width=15,
            bg=self.color_blanco,
            fg=self.color_azul_oscuro,
            insertbackground=self.color_naranja
        )
        self.entry_num2.grid(row=1, column=1, padx=5, pady=5)
        
        # Marco para botones
        marco_botones = tk.Frame(self.root, bg=self.color_fondo)
        marco_botones.pack(pady=20)
        
        # Botón Suma
        btn_suma = tk.Button(
            marco_botones,
            text="➕ Suma",
            font=("Arial", 12, "bold"),
            bg=self.color_azul,
            fg=self.color_blanco,
            activebackground=self.color_azul_oscuro,
            activeforeground=self.color_blanco,
            width=12,
            height=2,
            cursor="hand2",
            command=lambda: self.realizar_operacion("suma")
        )
        btn_suma.grid(row=0, column=0, padx=5, pady=5)
        
        # Botón Resta
        btn_resta = tk.Button(
            marco_botones,
            text="➖ Resta",
            font=("Arial", 12, "bold"),
            bg=self.color_naranja,
            fg=self.color_blanco,
            activebackground=self.color_naranja_claro,
            activeforeground=self.color_blanco,
            width=12,
            height=2,
            cursor="hand2",
            command=lambda: self.realizar_operacion("resta")
        )
        btn_resta.grid(row=0, column=1, padx=5, pady=5)
        
        # Botón Multiplicación
        btn_multiplicacion = tk.Button(
            marco_botones,
            text="✖️ Multiplicación",
            font=("Arial", 12, "bold"),
            bg=self.color_naranja_claro,
            fg=self.color_blanco,
            activebackground=self.color_naranja,
            activeforeground=self.color_blanco,
            width=12,
            height=2,
            cursor="hand2",
            command=lambda: self.realizar_operacion("multiplicacion")
        )
        btn_multiplicacion.grid(row=1, column=0, padx=5, pady=5)
        
        # Botón División
        btn_division = tk.Button(
            marco_botones,
            text="➗ División",
            font=("Arial", 12, "bold"),
            bg=self.color_azul_oscuro,
            fg=self.color_blanco,
            activebackground=self.color_azul,
            activeforeground=self.color_blanco,
            width=12,
            height=2,
            cursor="hand2",
            command=lambda: self.realizar_operacion("division")
        )
        btn_division.grid(row=1, column=1, padx=5, pady=5)
        
        # Marco para resultado
        marco_resultado = tk.Frame(self.root, bg=self.color_fondo)
        marco_resultado.pack(pady=20)
        
        tk.Label(
            marco_resultado,
            text="Resultado:",
            font=("Arial", 14, "bold"),
            bg=self.color_fondo,
            fg=self.color_azul_oscuro
        ).pack(pady=5)
        
        self.label_resultado = tk.Label(
            marco_resultado,
            text="---",
            font=("Arial", 20, "bold"),
            bg=self.color_blanco,
            fg=self.color_naranja,
            width=20,
            height=2,
            relief="raised",
            bd=3
        )
        self.label_resultado.pack(pady=5)
        
        # Botón limpiar
        btn_limpiar = tk.Button(
            self.root,
            text="🧹 Limpiar",
            font=("Arial", 11, "bold"),
            bg=self.color_azul,
            fg=self.color_blanco,
            activebackground=self.color_azul_oscuro,
            activeforeground=self.color_blanco,
            width=15,
            height=1,
            cursor="hand2",
            command=self.limpiar
        )
        btn_limpiar.pack(pady=10)
    
    def realizar_operacion(self, operacion):
        try:
            num1 = int(self.entry_num1.get())
            num2 = int(self.entry_num2.get())
            
            if operacion == "suma":
                resultado = num1 + num2
                self.label_resultado.config(text=str(resultado), fg=self.color_azul)
            elif operacion == "resta":
                resultado = num1 - num2
                self.label_resultado.config(text=str(resultado), fg=self.color_naranja)
            elif operacion == "multiplicacion":
                resultado = num1 * num2
                self.label_resultado.config(text=str(resultado), fg=self.color_azul_oscuro)
            elif operacion == "division":
                if num2 != 0:
                    resultado = num1 / num2
                    self.label_resultado.config(text=f"{resultado:.2f}", fg=self.color_naranja_claro)
                else:
                    messagebox.showerror("Error", "No se puede dividir por cero")
                    self.label_resultado.config(text="Error", fg="red")
                    
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos")
            self.label_resultado.config(text="Error", fg="red")
    
    def limpiar(self):
        self.entry_num1.delete(0, tk.END)
        self.entry_num2.delete(0, tk.END)
        self.label_resultado.config(text="---", fg=self.color_naranja)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
