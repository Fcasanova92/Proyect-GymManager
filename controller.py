from model import *

from tkinter import *

from tkinter import messagebox as MessageBox

from datetime import *

import re

# es esta clase se controlan las excepciones y los errores

class CONTROLLER (ALUMNO):

    def Agregar_alumno(self):

        try:    
            super().AGREGAR()

            MessageBox.showwarning("Alerta", 
    "Alumno agregado")


        except:

            MessageBox.showerror("Error", 
    "El alumno ya existe")



    def ACTUALIZAR(self):

        try:
            super().ACTUALIZAR()

            MessageBox.showwarning("Alerta", 
    "Alumno actualizado")


        except:

            MessageBox.showerror("Error", 
    "No es alumno del gimnasio")


    def BUSCAR(self):
        try:
            super().BUSCAR()

        except:

            MessageBox.showerror("Error", 
    "No es alumno del gimnasio")


    def BORRAR(self):

        super().BORRAR()

        MessageBox.showwarning("Alerta", 

    "Alumno eliminado")

    

    def VIEW_ALUMNO(self):

        super().VIEW_ALUMNO()

        if self.dias_suscrip == 0:

            MessageBox.showwarning("Alerta", 
    "Cuota Vencida")

        else: 

            MessageBox.showwarning("TUGYM", 
    "Bienvenido al gimnasio")












        





      


























