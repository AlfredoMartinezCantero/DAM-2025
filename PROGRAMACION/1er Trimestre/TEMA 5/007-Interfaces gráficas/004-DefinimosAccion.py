
import tkinter as tk
def accion():
    print("Bienvenido al mejor github del mundo, adelante: https://github.com//jocarsa ")
ventana = tk.Tk()

tk.Button(ventana,text="Púlsame si te atreves",command=accion).pack(padx=10,pady=10)

ventana.mainloop() # No te salgas


