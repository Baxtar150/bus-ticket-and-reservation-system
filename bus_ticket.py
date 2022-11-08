import tkinter as Tk
from tkinter import *
from tkinter import messagebox, ttk
from ttkthemes import ThemedTk

#,style="Framebg.TFrame"
def busticket():
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


    rt.mainloop()


# def Select_bus_number():
#     bus=[1001,1002,1003,1004,1005]
#     x=int(input())
#     for i in bus:
#        if i== 1001:
#            if i==x:
#                print("me")
# Select_bus_number()



# tno = Label(frame_Booking_Panel)
# tno.place(relx=0.19, rely=0.18, height=21, width=37)
# # tno.configure(background="#ffff00")
# tno.configure(font=(18))
# tno.configure(textvariable=ticketno)


# bus_id = Label(frame_Booking_Panel)
# bus_id.place(relx=0.75, rely=0.16, height=21, width=119)
# # bus_id.configure(background="#ffff00")
# bus_id.configure(font=(18))
# bus_id.configure(text="Bus : GKC001")


# font10 = "-family {Wide Latin} -size 10 -weight bold -slant "  \
#             "roman -underline 0 -overstrike 0"
# font15 = "-family {Snap ITC} -size 20 -weight bold -slant "  \
#             "roman -underline 1 -overstrike 0"
# font17 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
#             "roman -underline 0 -overstrike 0"
# font18 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
#             "roman -underline 0 -overstrike 0"

# self.bus_Service = Label(self.frame_Booking_Panel)
# self.bus_Service.place(relx=0.14, rely=0.05, height=21, width=544)
# self.bus_Service.configure(background="#808080")
# self.bus_Service.configure(font=font15)
# self.bus_Service.configure(text="Jam-Free Bus Service")

# frame_Booking_Panel.configure(relief=GROOVE)
# frame_Booking_Panel.configure(borderwidth="5")
# frame_Booking_Panel.configure(background="#808080")


# with open('Tickets.txt') as infile:
#     characters = 0
#     for lineno, line in enumerate(infile, 1):
#         wordslist = line.split()
#         characters += sum(len(word) for word in wordslist)
ticketno = StringVar()
# ticket_number = characters
# ticketno.set(ticket_number)


    
    
    # if(dbQuery.empty(Name.get()) == True or dbQuery.empty(Email.get()) == True or dbQuery.empty(Phone.get())== True or dbQuery.empty(Gender.get())==True or dbQuery.empty(Marital_status.get())== True or dbQuery.empty(DObirth.get())== True or dbQuery.empty(Password.get())== True):
    #     messagebox.showwarning('Empyt Field', 'The field is required please fill.')
    #     return
    # if not(Password.get()==Repeatpass.get()):
    #     messagebox.showwarning('UnMatch Password', 'The password does not match.')
    #     return
        
    # if(dbQuery.match(Password.get(),Repeatpass.get()) == False):
    #     messagebox.showwarning('UnMatch Password', 'The password does not match.')
    #     return
    
    # if Email.get():
    #     messagebox.showwarning('Record Exist', 'The email used is already exist!')
    #     return
    # if(dbQuery.checkEmail(Email.get())== True):
    #     messagebox.showwarning('Record Exist', 'The email used is already exist!')
    #     return
    