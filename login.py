import tkinter as Tk
from tkinter import *
from tkinter import messagebox, ttk
from ttkthemes import ThemedTk
import control.Controllerdb as db
import dashboard 
# from dashboard import display_dash
import register

def logingui():
    def clickhere():
        rt.destroy()
        register()

    def signIn():
            dbQuery = db.controller()
            if(Email.get())=="" or (Password.get()== ""):
                messagebox.showwarning('Empty Field', 'The field(s) are required.')
                return    
            query = "SELECT * FROM users WHERE email=%s AND password=%s"
            values=(Email.get(),Password.get())
            rs = dbQuery.getLogin(query,values)
            if rs==None:
                messagebox.showerror('Error Login', 'Password or Email is INVALID')
                return
            if(rs):
                messagebox.showinfo('Success', 'Your login is successful.')
                Email.set('')
                Password.set('')
                rt.destroy()
            
            else:
                messagebox.showerror('Error Login', 'Password or Exam No is INVALID')
#,style="Framebg.TFrame"

    global rt
    rt =ThemedTk(theme='adapta', themebg=True)
    rt.title("JayTeeOjo Transportation")
    width = 450
    height = 400
    sw = rt.winfo_screenwidth()
    sh = rt.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    rt.geometry(f'{width}x{height}+{x}+{y}')
    rt.resizable(0, 0)

    style=ttk.Style()
    style.configure("titlelbl.TLabel", font=("Arial",22,"bold"))
    style.configure("loginlbl.TLabel", font=("Arial",14,"bold"))
    style.configure("Framebg.TFrame",background="blue")
    style.configure("registerbtn.TButton",font=("Arial",12,"bold"))
    style.configure("loginbtn.TButton", font=("Arial",14,"bold"),background="red")

    titleframe=ttk.Frame(rt)
    titleframe.pack(pady=(5,0))
    loginframe= ttk.Frame(rt)
    loginframe.pack(pady=(0,5))
    buttonframe= ttk.Frame(rt, width=400,height=100)
    buttonframe.pack(pady=(0,5))
    
    global Email,Password
    Email=StringVar()
    Password=StringVar()

    loginlbl=ttk.Label(titleframe, text="Login", style="titlelbl.TLabel")
    loginlbl.pack(pady=(20,0))

    emaillbl=ttk.Label(loginframe, text="Email", style="loginlbl.TLabel")
    emaillbl.pack(pady=(20,0))
    emailenrtry=ttk.Entry(loginframe,width=20,font=(10), textvariable=Email)
    emailenrtry.pack(pady=(0,10))

    passwordlbl=ttk.Label(loginframe, text="Password", style="loginlbl.TLabel")
    passwordlbl.pack(pady=(20,0))
    passwordenrtry=ttk.Entry(loginframe,width=20,font=(10),textvariable=Password)
    passwordenrtry.pack(pady=(0,10))


    registerlbl=ttk.Label(buttonframe,text="Are you registered?", style="loginlbl.TLabel")
    registerlbl.place(x=70,y=70)
    loginbtn=ttk.Button(buttonframe, text="Login", width=19,style="loginbtn.TButton",command=signIn)
    loginbtn.place(x=84,y=10)
    registerbtn=ttk.Button(buttonframe,text="Click here",style="registerbtn.TButton",command=clickhere)
    registerbtn.place(x=257, y=60)

    rt.mainloop()
# logingui()