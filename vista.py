
from tkinter import *

from controller import CONTROLLER

from datetime import *

# Clase que desarrolla unicamente la interfaz

class INTERFAZ(CONTROLLER):

    # Constructor de la clase interfaz (contruye la interfaz)

    def __init__(self):

        # estos atributos del constructor desarrollan la raiz o fram principal de la interfaz

        self.root = Tk()

        self.root.geometry("1200x720")     

        self.root.resizable(0,0) 

        self.root.title("TuGYM") 

        self.bar_menu = Menu(self.root)

        self.root.config(relief = "sunken", borderwidth = 10, menu=self.bar_menu, bg="ivory2")

        icono = PhotoImage(file="png-transparent-dumbbells-gym-sport-weight-sports-icon.png")

        icono2= PhotoImage(file="png-transparent-logo-event-planning-fitness-centre-protocol-gym-text-logo-monochrome (1).png")

        self.root.iconphoto(True, icono)

        title = Label(self.root, text = "BIENVENIDO A TUGYM", bg= "ivory2", font=("CASTELLAR",40) )

        title.place(x=240 , y=50 ,  width="700", height="50")

        image = Label(self.root, width="150", height="100", image = icono2 )

        image.place(x=967, y=30)

        self.day_now = Label(self.root, text="  ", font=("Rockwell", 15), bg="ivory2")
                
        self.day_now.place(x=450, y=100, width="90" , height="50")

        self.date_now = Label(self.root, text="  ", font=("Rockwell", 15), bg="ivory2")
                
        self.date_now.place(x=550, y=100, width="90" , height="50")

        self.text_time = Label(self.root, text="  ", font=("Rockwell", 15), bg="ivory2")
                
        self.text_time.place(x=650, y=100, width="90" , height="50")

        # Estos metodos llamados en el constructor desarrollan otras partes secundarias de la interfaz

        self.frame_inf()

        self.menu()

        self.frame_sup()

        self.update_time()
        
        self.root.mainloop()




    def frame_sup(self):

        # Estos metodos desarrolla el frame superior, el cual tiene los datos que se muestran cuando se ingresa el dni

        frame1 = Frame(self.root,width="1000", height="400", bg = "ivory3", relief = "solid", borderwidth = 5)

        frame1.place(x=120, y=140)


        bienvenido_alumno = Label(frame1, text="ALUMNO ", font=("Rockwell", 20), bg="ivory3")
        
        bienvenido_alumno.place(x=2, y=20, width="500", height="50")

        self.nombre_bienvenida = StringVar()

        nombre_bienvenida = Entry(frame1, font=("Rockwell", 20), bg = "ivory3", state="readonly", textvariable = self.nombre_bienvenida)

        nombre_bienvenida.place(x=380, y=20 , width="500", height="50")


        bienvenido_rutina = Label(frame1, text="RUTINA ", font=("Rockwell", 20), bg="ivory3")
        
        bienvenido_rutina.place(x=40, y=90, width="400", height="50")

        self.rutina_bienvenida = StringVar()

        rutina = Entry(frame1, font=("Rockwell", 15), bg = "ivory3", state="readonly", textvariable = self.rutina_bienvenida)

        rutina.place(x=380, y=90 , width="500", height="220")



        dias_vencimiento = Label(frame1, text="VENCIMIENTO ", font=("Rockwell", 20), bg="ivory3")

        dias_vencimiento.place(x=127, y=330, width="300", height="50")

        self.vencimiento = StringVar()


        suscr_bienvenida = Entry(frame1, font=("Rockwell", 20), bg = "ivory3", state="disable", textvariable = self.vencimiento)

        suscr_bienvenida.place(x=380, y=330 , width="150", height="50")


        
    def update_time(self):

        # Estos metodo configura el aspecto de la fecha y hora de la interfaz ( el reloj que se ve)

        self.time = datetime.now()
            
        self.hora= self.time.strftime("%H:%M:%S")

        self.text_time.configure(text=self.hora)

            
        self.date = self.time.strftime("%d/%m/%y")

        self.date_now.configure(text=self.date)


        self.day = self.time.strftime("%A")

        if self.day == "Monday":

                self.day = "Lunes"

                self.day_now.configure(text = self.day)


        elif self.day == "Tuesday":

                self.day = "Martes"

                self.day_now.configure(text = self.day)

        elif self.day == "Wednesday":

            self.day = "Miercoles"

            self.day_now.configure(text = self.day)


        elif self.day == "Thursday":

            self.day = "Jueves"

            self.day_now.configure(text = self.day)


        elif self.day == "Friday":

             self.day = "Viernes"

             self.day_now.configure(text = self.day)


        elif self.day == "Saturday":

             self.day = "Sabado"

             self.day_now.configure(text = self.day)


        self.root.after(1000, self.update_time )


        
    def frame_inf(self):

        # Estos metodo configura el frame inferior, donde se busca el dni y se observa los dias que le quedan de suscripcion


        Frame2 = Frame(self.root, width="1000", height="150", bg = "ivory3", relief = "solid", borderwidth = "5")

        Frame2.place(x=120, y=550)


        text_dni2 = Label(Frame2, text="DNI : ", font=("Rockwell", 30), bg="ivory3")
                
        text_dni2.place(x=10, y=35, width="100" , height="50")

        self.dni_entry = StringVar()


        entrada_dni=Entry(Frame2 ,font=("Rockwell", 30),bg="ivory3", textvariable = self.dni_entry)

        entrada_dni.place(x=110, y=45, width = "250", height="40")


        botton_entry_dni = Button(Frame2, text= "OK", font=("Rockwell", 15), relief="sunken", borderwidth="10", bg="ivory3", foreground="black", command=self.VIEW_ALUMNO)

        botton_entry_dni.place(x=380, y=45, width=50, height=40)



        text_vencimiento = Label(Frame2, text="Días restantes de suscripcion en el gimnasio :  ", font=("Rockwell", 15), bg="ivory3")
                
        text_vencimiento.place(x=430, y=35, width="500" , height="50")

        self.dias_vencimiento = StringVar()


        self.vencimiento = Entry(Frame2 ,font=("Rockwell", 15),bg="ivory3", state="readonly", textvariable = self.dias_vencimiento)

        self.vencimiento .place(x=900, y=40, width = "30", height="40")



    def menu(self):

        # Estos metodo configura la barra del menu

        gestionfile = Menu(self.bar_menu, tearoff=0)

        helpmenu= Menu(self.bar_menu,tearoff=0)

        self.bar_menu.add_cascade(label="Inicio", menu=gestionfile)

        self.bar_menu.add_cascade(label="Ayuda", menu = helpmenu)

        gestionfile.add_separator()

        gestionfile.add_command(label="Gestion Alumno", command=self.gestion_alumnos)  

        gestionfile.add_command(label="Gestion Gimnasio")

        gestionfile.add_command(label = "Salir", command= self.root.quit)



    def gestion_alumnos(self):

         # Estos metodo configura la pestaña de gestion de alumnos


        self.window=Toplevel(self.root,width="600", height="900", bg = "ivory3", relief = "solid", borderwidth = 5) 

        self.window.resizable(0,0) 

        self.window.title("GESTION DE ALUMNOS") 


        boton_agregar = Button(self.window, text= "AGREGAR", font=("Rockwell", 10), relief="sunken", borderwidth="10", bg="ivory4", foreground="black")

        boton_agregar.place(x=27, y=800, width=100, height=70)


        boton_actualizar = Button(self.window, text= "ACTUALIZAR", font=("Rockwell", 10), relief="sunken",borderwidth="10", bg="ivory4", foreground="black")

        boton_actualizar.place(x=167, y=800, width=100, height=70)


        boton_borrar = Button(self.window, text= "BORRAR", font=("Rockwell", 10),relief="sunken", borderwidth="10", bg="ivory4", foreground="black")

        boton_borrar.place(x=312, y=800, width=100, height=70)


        boton_buscar = Button(self.window, text= "BUSCAR", font=("Rockwell", 10),relief="sunken", borderwidth="10", bg="ivory4", foreground="black")

        boton_buscar.place(x=457, y=800, width=100, height=70)




        text_dni = Label(self.window, text="DNI  ", font=("Rockwell", 15),bg = "ivory3")
                
        text_dni .place(x=50,y=50)

        self.DNI = StringVar()

        entry_DNI = Entry(self.window, textvariable = self.DNI)

        entry_DNI.place(x=250,y=55,width=200, height=20)



        text_nombre = Label(self.window, text="Nombre ", font=("Rockwell", 15),bg = "ivory3")
                
        text_nombre.place(x=50,y=100)

        self.nombre = StringVar()

        entry_nombre=Entry(self.window, textvariable = self.nombre)

        entry_nombre.place(x=250,y=105, width=200, height=20)

            

        text_apellido = Label(self.window, text="Apellido  ", font=("Rockwell", 15), bg = "ivory3")

        text_apellido.place(x=50,y=150)

        self.apellido = StringVar()

        entry_apellido=Entry(self.window , textvariable = self.apellido)

        entry_apellido.place(x=250,y=150, width=200, height=20)


        text_telefono = Label(self.window, text="Telefono  ", font=("Rockwell", 15),bg = "ivory3")
                
        text_telefono.place(x=50,y=200)

        self.telefono = StringVar()

        entry_telefono = Entry(self.window, textvariable = self.telefono)

        entry_telefono.place(x=250,y=205,width=200, height=20)


        text_email = Label(self.window, text="Email  ", font=("Rockwell", 15),bg = "ivory3")
                
        text_email.place(x=50,y=250)
            
        self.email = StringVar()

        entry_email=Entry(self.window, textvariable = self.email)

        entry_email.place(x=250,y=255, width=200, height=20)


        text_pago = Label(self.window, text="Fecha de Inscripción  ", font=("Rockwell", 15), bg = "ivory3")
                
        text_pago.place(x=50,y=300)
            
        self.pago = StringVar()

        entry_pago=Entry(self.window, textvariable = self.pago)

        entry_pago.place(x=250,y=305, width=200, height=20)


        text_rutina = Label(self.window, text = "Rutina ", font=("Rockwell", 15), bg="ivory3")

        text_rutina.place(x=50, y=350)

        self.rutina = StringVar()

        self.entry_rutina = Entry(self.window, font=("Rockwell", 15), textvariable = self.rutina )

        self.entry_rutina.place(x=250, y=355, width=300, height=400)

        self.window.mainloop()



proyecto = INTERFAZ()



