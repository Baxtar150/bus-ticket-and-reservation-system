import tkinter as Tk
from tkinter import *
from tkinter import messagebox, ttk
from ttkthemes import ThemedTk
import control.Controllerdb as db
from PIL import Image,ImageTk  

def viewbooked():
    global rt
    rt =ThemedTk(theme='adapta', themebg=True)
    rt.title("JayTeeOjo Transportation")
    width = 450
    height = 350
    sw = rt.winfo_screenwidth()
    sh = rt.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    rt.geometry(f'{width}x{height}+{x}+{y}')
    rt.resizable(0, 0)
    
    style=ttk.Style()
    style.configure("loginlbl.TLabel", font=("Arial",14,"bold"))
    style.configure("loginlbl.TButton", font=("Arial",14,"bold")) 
     
    img=Image.open("img/bus_blur2.png")
    imgsize=img.resize((450,350))
    imgtp= ImageTk.PhotoImage(imgsize)

    LogoLabel = ttk.Label(rt,image=imgtp)
    LogoLabel.place(x=0,y=0,relheight=1,relwidth=1)
    
    ticketlbl=ttk.Label(rt, text="Enter Ticket No", style="loginlbl.TLabel")
    ticketlbl.pack(pady=(110,5))
    
    ticketenrtry=ttk.Entry(rt,width=20,font=(10))
    ticketenrtry.pack(pady=(5,10))
    
    ticketbtn=ttk.Button(rt,text="Enter",style="loginlbl.TButton")
    ticketbtn.pack()
    
    rt.mainloop()
viewbooked()

def displayview():
    rt =ThemedTk(theme='adapta', themebg=True)
    rt.title("JayTeeOjo Transportation")
    width = 450
    height = 350
    sw = rt.winfo_screenwidth()
    sh = rt.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    rt.geometry(f'{width}x{height}+{x}+{y}')
    rt.resizable(0, 0)
    
    
    rt.mainloop()