import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()


arbol = ttk.Treeview(ventana,columns=("nombre", "apellidos"), show="headings")
arbol.heading("nombre", text="Nombre del cliente")
arbol.heading("apellidos", text="Apellidos del cliente")

arbol.insert("", "end", values=("Alfredo", "Martínez Cantero"))
arbol.insert("", "end", values=("Rafa", "Cantero Trullenque"))

arbol.pack(padx=20,pady=20)

ventana.mainloop()

