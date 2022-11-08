import tkinter as Tk
from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import *
from ttkthemes import ThemedTk

rt =ThemedTk(theme='adapta', themebg=True)
rt.title("JayTeeOjo Transportation")
width = 600
height = 490
sw = rt.winfo_screenwidth()
sh = rt.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
rt.geometry(f'{width}x{height}+{x}+{y}')
rt.resizable(0, 0)
# rt.overrideredirect(True)

style=ttk.Style()
style.configure("Framebg.TFrame",background="blue")
style.configure("Framebg2.TFrame",background="red")
style.configure("inputregister.TLabel", font=("Arial",14,"bold"))
style.configure("inputregister.TFrame", font=(14))
style.configure("inputlogin.TButton", font=("Arial",14,"bold"),background="red")

registrationframe= ttk.Frame(rt)
registrationframe.pack(pady=5)
inputframe=ttk.Frame(rt,width=500, height=70)
inputframe.pack()

registerframe= ttk.Frame(registrationframe)
registerframe.pack(pady=5)
#,style="Framebg.TFrame",,,  ,style="Framebg2.TFrame", ,style="Framebg.TFrame"
inputregister=ttk.Frame(registrationframe)
inputregister.pack(pady=5)

#creating registartion labels 
#palced text=Register in a different frame
registerlbl=ttk.Label(registerframe, text="Register", font=("Arial",22,"bold"))
registerlbl.grid()


#Stringvar
global Name,Email,Phone,Gender,Marital_status,DObirth,Password,Repeatpass
bus_id=StringVar()
bus_type=StringVar()
bus_color=StringVar()
bus_seat=StringVar()
bus_route=StringVar()


#Form content inputregister frame
busidlbl=ttk.Label(inputregister,text="Name",style="inputregister.TLabel")
busidlbl.grid(row=0,column=0, sticky="WE")
bustypelbl=ttk.Label(inputregister,text="Email",style="inputregister.TLabel")
bustypelbl.grid(row=1,column=0, sticky="WE")
buscolorlbl=ttk.Label(inputregister,text="Phone",style="inputregister.TLabel")
buscolorlbl.grid(row=2,column=0,sticky="WE")
busseatlbl=ttk.Label(inputregister,text="Gender",style="inputregister.TLabel")
busseatlbl.grid(row=3,column=0,sticky="WE")
statuslbl=ttk.Label(inputregister,text="Marital Status",style="inputregister.TLabel")
statuslbl.grid(row=4,column=0,sticky="WE")
doblbl=ttk.Label(inputregister,text="Date of Birth",style="inputregister.TLabel")
doblbl.grid(row=5,column=0, sticky="WE")
passwordlbl=ttk.Label(inputregister,text="Password",style="inputregister.TLabel")
passwordlbl.grid(row=6,column=0, sticky="WE")
repasswordlbl=ttk.Label(inputregister,text="Password",style="inputregister.TLabel")
repasswordlbl.grid(row=7,column=0, sticky="WE")

# nameentry=ttk.Entry(inputregister,width=30,justify="center",textvariable=Name, font=(10))
# nameentry.grid(row=0, column=1,sticky="WE",pady=5)
# emailentry=ttk.Entry(inputregister,width=30,justify="center",textvariable=Email,font=(10))
# emailentry.grid(row=1, column=1,sticky="WE",pady=5)
# phoneentry=ttk.Entry(inputregister,width=30,justify="center",textvariable=Phone,font=(10))
# phoneentry.grid(row=2, column=1,sticky="WE",pady=5)
# genderentry=ttk.Combobox(inputregister, values=("Male","Female"), state='readonly',textvariable=Gender)
# genderentry.grid(row=3, column=1, sticky='WE', pady=(0, 5))
# statusentry=ttk.Combobox(inputregister, values=("Single","Married","Divorced"), state='readonly',textvariable=Marital_status)
# statusentry.grid(row=4, column=1, sticky='WE', pady=(0, 5))
# dobentry=DateEntry(inputregister,textvariable=DObirth)
# dobentry.grid(row=5, column=1,sticky='WE', pady=(0, 5))
# passwordentry=ttk.Entry(inputregister,width=30,justify="center",textvariable=Password, font=(10),show="$")
# passwordentry.grid(row=6, column=1,sticky="WE",pady=5)
# repasswordentry=ttk.Entry(inputregister,width=30,justify="center",textvariable=Repeatpass, font=(10))
# repasswordentry.grid(row=7, column=1,sticky="WE",pady=5)


submitbtn=ttk.Button(inputframe,text="Sign Up",style="inputlogin.TButton")
submitbtn.place(x=350,y=0)
loginbn=ttk.Button(inputframe,text="Login",style="inputlogin.TButton")
loginbn.place(x=200,y=0)
clearbtn=ttk.Button(inputframe,text="Clear",style="inputlogin.TButton")
clearbtn.place(x=50,y=0)


rt.mainloop()