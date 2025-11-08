import tkinter as tk

ventana = tk.Tk()

ventana.title("Suma de dos números")
ventana.geometry("350x150")

etiqueta1 = tk.Label(ventana, text="Número 1:")
etiqueta1.pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

etiqueta2 = tk.Label(ventana, text="Número 2:")
etiqueta2.pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

def calcular_suma():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        etiqueta_resultado.config(text="Error: ingrese solo números")

boton_calcular = tk.Button(ventana, text="Calcular Suma", command=calcular_suma)
boton_calcular.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()
ventana.mainloop()  