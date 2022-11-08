import tkinter
from tkinter import ttk
from tkinter import *
from ttkthemes import THEMES, ThemedTk
from PIL import Image,ImageTk
# import login
# End of module importation

#function loading  
def progress():
    pb['value'] +=25
    if pb['value'] == 100:
        # pb.stop()
        # rt.destroy()
        # login.loginApp()
        return
    pb.after(1000, progress)
#Colours and conetents importation 
__primary = '#87CEEB'

#Starting Tk function for drawing the interface
rt = ThemedTk(theme='adapta', themebg=True)
width = 475
height = 322
sw = rt.winfo_screenwidth()
sh = rt.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
rt.geometry(f'{width}x{height}+{x}+{y}')
rt.resizable(0, 0)
rt.overrideredirect(True)

img=Image.open("img/bus_blur2.png")
imgsize=img.resize((280,189))
imgtp= ImageTk.PhotoImage(imgsize) 
LogoLabel = ttk.Label(rt,image=imgtp)
LogoLabel.place(relx=0.2,rely=0.2) 

#Placing Logo and Icons 


#placing content on frame
# splashFrame = ttk.Frame(rt,width=400)
# splashFrame.pack(pady=10)

#Initializing styling for ttk elements
style = ttk.Style()
style.configure('label1.TLabel', font=('roboto', 24, 'bold'),foreground=__primary)
style.configure('copyright.TLabel', font=('roboto',16,'normal'),foreground=__primary)

# #placing Label on the SplashFrame 
splashLabel1 = ttk.Label(rt, text='JayTeeOjo Transportation ', style='label1.TLabel')
splashLabel1.pack(pady=5)

lblcopyright = ttk.Label(rt, text= 'Securedtransport- 2022', style='copyright.TLabel')
lblcopyright.place(relx=0.25,rely=0.85)

pb = ttk.Progressbar(rt,mode='determinate',orient='horizontal',maximum=100,value=0)
pb.place(relx=0, rely=0.94,height=10,relwidth=1)


#starting the loading content 
progress()
#end loading
rt.mainloop()
