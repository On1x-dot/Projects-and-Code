import tkinter as tk
from tkinter import messagebox

# Funciones para las operaciones
def click_boton(num):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(num))

def limpiar_entrada():
    entrada.delete(0, tk.END)

def suma():
    global primer_numero
    global operacion
    operacion = "suma"
    primer_numero = float(entrada.get())
    entrada.delete(0, tk.END)

def resta():
    global primer_numero
    global operacion
    operacion = "resta"
    primer_numero = float(entrada.get())
    entrada.delete(0, tk.END)

def multiplicacion():
    global primer_numero
    global operacion
    operacion = "multiplicacion"
    primer_numero = float(entrada.get())
    entrada.delete(0, tk.END)

def division():
    global primer_numero
    global operacion
    operacion = "division"
    primer_numero = float(entrada.get())
    entrada.delete(0, tk.END)

def igual():
    segundo_numero = float(entrada.get())
    entrada.delete(0, tk.END)

    if operacion == "suma":
        entrada.insert(0, primer_numero + segundo_numero)
    elif operacion == "resta":
        entrada.insert(0, primer_numero - segundo_numero)
    elif operacion == "multiplicacion":
        entrada.insert(0, primer_numero * segundo_numero)
    elif operacion == "division":
        if segundo_numero != 0:
            entrada.insert(0, primer_numero / segundo_numero)
        else:
            messagebox.showerror("Error", "División por cero no permitida")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")

# Crear el cuadro de texto donde se verá el resultado
entrada = tk.Entry(ventana, width=35, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones numéricos
botones = [
    '7', '8', '9', '4', '5', '6', '1', '2', '3', '0'
]

fila = 1
columna = 0

for numero in botones:
    boton = tk.Button(ventana, text=numero, padx=20, pady=20, command=lambda num=numero: click_boton(num))
    boton.grid(row=fila, column=columna)

    columna += 1
    if columna == 3:
        columna = 0
        fila += 1

# Botones de operaciones
boton_suma = tk.Button(ventana, text="+", padx=20, pady=20, command=suma)
boton_resta = tk.Button(ventana, text="-", padx=20, pady=20, command=resta)
boton_multiplicacion = tk.Button(ventana, text="*", padx=20, pady=20, command=multiplicacion)
boton_division = tk.Button(ventana, text="/", padx=20, pady=20, command=division)
boton_igual = tk.Button(ventana, text="=", padx=20, pady=20, command=igual)
boton_limpiar = tk.Button(ventana, text="C", padx=20, pady=20, command=limpiar_entrada)

# Colocar botones de operaciones
boton_suma.grid(row=1, column=3)
boton_resta.grid(row=2, column=3)
boton_multiplicacion.grid(row=3, column=3)
boton_division.grid(row=4, column=3)
boton_igual.grid(row=4, column=2)
boton_limpiar.grid(row=4, column=0)

# Ejecutar la ventana
ventana.mainloop()
