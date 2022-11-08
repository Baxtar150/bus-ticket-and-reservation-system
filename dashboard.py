import tkinter as Tk
from tkinter import *
from tkinter import messagebox, ttk
from ttkthemes import ThemedTk
from PIL import Image,ImageTk
#,style="Framebg.TFrame"
def display_dash():
    rt =ThemedTk(theme='adapta', themebg=True)
    rt.title("JayTeeOjo Transportation")
    width = 695
    height = 480
    sw = rt.winfo_screenwidth()
    sh = rt.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    rt.geometry(f'{width}x{height}+{x}+{y}')
    rt.resizable(0, 0)

    style=ttk.Style()
    style.configure("ticketbtn.TButton", font=("Arial",15,"bold"))
    style.configure("loginlbl.TLabel", font=("Arial",14,"bold"))

    img=Image.open("img/bus_blur2.png")
    imgsize=img.resize((695,480))
    imgtp= ImageTk.PhotoImage(imgsize)

    img2=Image.open("img/bus_blur2.png")
    imgsize2=img2.resize((230,150))
    imgtp2= ImageTk.PhotoImage(imgsize2)

    LogoLabel = ttk.Label(rt,image=imgtp)
    LogoLabel.place(x=0,y=0,relheight=1,relwidth=1)


    ticket_btn=ttk.Button(rt, text="Bus Ticket",style="ticketbtn.TButton")
    ticket_btn. place(x=30,y=390,height=60)
    ticket_btn=ttk.Button(rt, text="View Ticket",style="ticketbtn.TButton")
    ticket_btn. place(x=200,y=390,height=60)
    ticket_btn=ttk.Button(rt, text="Terminals",style="ticketbtn.TButton")
    ticket_btn. place(x=370,y=390,height=60)
    supportbtn=ttk.Button(rt, text="Support",style="ticketbtn.TButton")
    supportbtn. place(x=540,y=390,height=60)
    rt.mainloop()
display_dash()