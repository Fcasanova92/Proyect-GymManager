import sqlite3


from datetime import datetime, timedelta

import re

from tkinter import messagebox as MessageBox

# Funciones verificadores de datos


# esta clase maneja los metodos que se activan en los botones de gestion de alumnos, interactuando con la base de datos

class ALUMNO:

    def AGREGAR (self):

        self.conexion = sqlite3.connect("Base de datos Alumnos Gym")
        
        self.cursor = self.conexion.cursor()

        fecha=datetime.now()

        self.fecha_pago = fecha.date()

        datos_alumno = self.DNI.get(), self.nombre.get(), self.apellido.get(), self.telefono.get(),  self.email.get(), self.fecha_pago , self.rutina.get()

        self.cursor.execute("INSERT INTO ALUMNOS VALUES (NULL,?,?,?,?,?,?,?)", (datos_alumno))

        self.conexion.commit()

        self.DELETE_FIELD()

        self.conexion.close()

       
    def BUSCAR(self):

        self.conexion = sqlite3.connect("Base de datos Alumnos Gym")
        
        self.cursor = self.conexion.cursor()

        self.cursor.execute("SELECT NOMBRE, APELLIDO, TELEFONO, EMAIL, FECHA, RUTINA FROM ALUMNOS WHERE DNI =" + self.DNI.get())

        datos = self.cursor.fetchall()

        for i in datos:
            
            self.nombre.set(i[0])
            
            self.apellido.set(i[1])
        
            self.telefono.set(i[2])
         
            self.email.set(i[3])

            self.pago.set(i[4])

            self.rutina.set(i[5])

        self.conexion.commit()

        self.conexion.close()


    def ACTUALIZAR(self):

        self.conexion = sqlite3.connect("Base de datos Alumnos Gym")
        
        self.cursor = self.conexion.cursor()

        datos_nuevos =  self.nombre.get(), self.apellido.get(), self.telefono.get(), self.email.get(), self.fecha_pago, self.rutina.get()

        self.cursor.execute("UPDATE ALUMNOS SET NOMBRE=?, APELLIDO=?, TELEFONO=?, EMAIL= ?, FECHA=? , RUTINA = ? WHERE DNI =" + self.DNI.get(),(datos_nuevos))

        self.conexion.commit()

        self.conexion.close()

        self.DELETE_FIELD()

    
    def BORRAR(self):

        self.conexion = sqlite3.connect("Base de datos Alumnos Gym")
        
        self.cursor = self.conexion.cursor()

        self.cursor.execute("DELETE FROM ALUMNOS WHERE DNI =" + self.DNI.get())

        self.conexion.commit()

        self.conexion.close()

        self.DELETE_FIELD()
        

# este metodo borra los campos cuando se agrega, actualiza, busca o borra un alumno

    def DELETE_FIELD(self):

        self.DNI.set(" ")

        self.nombre.set(" ")
        
        self.apellido.set(" ")
        
        self.telefono.set(" ") 
        
        self.email.set(" ")

        self.pago.set(" ")

        self.rutina.set(" ")


# este metodo muestra los datos cuando el alumno indica el dni para saber si puede ingresar o no al gimnasio

    def VIEW_ALUMNO(self):
        
        self.conexion = sqlite3.connect("Base de datos Alumnos Gym")
        
        self.cursor = self.conexion.cursor()

        self.cursor.execute("SELECT NOMBRE, APELLIDO, FECHA, RUTINA FROM ALUMNOS WHERE DNI =" + self.dni_entry.get())

        view_datos=self.cursor.fetchall()

        for i in view_datos:
            
            self.nombre_bienvenida.set(i[0] + " " + i[1])

            fecha_pago = i[2]

            self.rutina_bienvenida.set(i[3])


        fecha_pago = datetime.strptime(fecha_pago, "%Y-%m-%d")

        self.fecha_vencimiento = fecha_pago + timedelta(days=30)

        self.vencimiento.set(self.fecha_vencimiento)

        self.day_today = datetime.today()

        self.dias_suscrip = round(((self.fecha_vencimiento - self.day_today).total_seconds())/86400)

        self.dias_vencimiento.set(self.dias_suscrip)

        self.conexion.commit()

        self.conexion.close()   

