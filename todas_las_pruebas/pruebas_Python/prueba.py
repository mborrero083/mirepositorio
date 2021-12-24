"""from tkinter import *

raiz=Tk()
raiz.title("Mi primera venta")
raiz.resizable(1,1)#habilitar el ancho y el alto del tamaño
#raiz.geometry("650x350") #tamaño de ventana
raiz.config(bg="black")#color de vantana
miframe=Frame(raiz)
miframe.pack(fill="both",expan="true")
miframe.config(bg="white")
miframe.config(width="650",height="350")
miframe.config(bd="15")
texto=Label(miframe,text="TE AMO PILAR", fg="black",font=18)
texto.place(x="200",y="100")
raiz.mainloop()
"""

def convert(s, numRows):
    if numRows == 1:
            return s
    step = 1
    pos = 1
    lines = {}
    for c in s:
        if pos not in lines:
            lines[pos] = c
        else:
            lines[pos]+=c
        pos+=step
        if pos==1 or pos==numRows:
            step*=-1
    sol = ""
    for i in range(1, numRows+1):
        try:
            sol+=lines[i]
        except:
            return sol
    return sol
    


s="PAYPALISHIRING"
print (convert(s,3))
#"PAYPALISHIRING"

