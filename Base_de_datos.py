import sqlite3


conexion = sqlite3.connect("Base de datos Alumnos Gym")

cursor = conexion.cursor()

cursor.execute ("CREATE TABLE ALUMNOS (ID_ALUMNO INTIGER AUTO INCREMENT, DNI INTERGER PRIMARY KEY , NOMBRE VARCHAR (30), APELLIDO VARCHAR (40), TELEFONO INTERGER, EMAIL VARCHAR (30), FECHA DE PAGO DATE, RUTINA TEXT)")

conexion.close()




