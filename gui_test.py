from tkinter import *

ventana_principal = Tk()
ventana_principal.title('Base de Datos con Neo4j')
ventana_principal.geometry('500x500')

icono = PhotoImage(file = './img/burger.png')
ventana_principal.iconphoto(False, icono)

boton_salir = Button(ventana_principal, text='Sali', width=10, height=2, command=ventana_principal.destroy)
boton_salir.place(relx=0.5, rely=0.9, anchor = CENTER)

ventana_principal.mainloop()

"""
r = tk.Tk() 
r.title('Counting Seconds')
r.geometry("500x500")

icon = tk.PhotoImage(file = "./img/burger.png")
r.iconphoto(False, icon)
r.positionfrom()
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 
r.mainloop()
"""