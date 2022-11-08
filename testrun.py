from sre_parse import State
import string
import random
import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from ttkthemes import ThemedTk
import datetime as dt
from ttkthemes import ThemedTk
from PIL import Image,ImageTk
import control.Controllerdb as db



def booked():
    price=5000
    # s_west
    if Boarding.get()=='Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State' and Destination.get()=='Abia State'or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State':
        price=price
        print(price)
    # elif Destination.get()==('Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State' )and Boarding.get()==('Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State'):
    #     price=price
    # if (Boarding.get())==('Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State') and (Destination.get())==('Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State'):
    #     price=price+500
    # elif (Destination.get())==('Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State') and (Boarding.get())==('Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State'):
    #     price=price+500
    # elif Boarding.get()==('Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State') and Destination.get()==('Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State'):
    #     price=10500
    # elif Destination.get()==('Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State') and Boarding.get()==('Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State'):
    #     price=10500
    # elif Boarding.get()==('Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State') and Destination.get()==('Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State'):
    #     price=10000
    # elif Destination.get()==('Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State') and Boarding.get()==('Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State'):
    #     price=10000
    # elif Boarding.get()==('Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State') and Destination.get()==('Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT'):
    #     price=7000
    # elif Destination.get()==('Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State') and Boarding.get()==('Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT'):
    #     price=7000
    # #s_east to all
    # elif Boarding.get()==('Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State') and Destination.get()==('Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State'):
    #     price=7000
    # elif Destination.get()==('Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State') and Boarding.get()==('Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State'):
    #     price=7000
    # elif Boarding.get()==('Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State') and Destination.get()==('Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State'):
    #     price=12000
    # elif Destination.get()==('Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State') and Boarding.get()==('Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State'):
    #     price=12000
    # elif Boarding.get()==('Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State') and Destination.get()==('Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State'):
    #     price=15000
    # elif Destination.get()==('Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State') and Boarding.get()==('Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State'):
    #     price=15000
    # elif Boarding.get()==('Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State') and Destination.get()==('Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT'):
    #     price=9000
    # elif Destination.get()==('Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State') and Boarding.get()==('Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT'):
    #     price=9000
    # #s_west
    # elif Boarding.get()==('Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State') and Destination.get()==('Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State'):
    #     price=20000
    # elif Destination.get()==('Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State') and Boarding.get()==('Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State'):
    #     price=20000
    # elif Boarding.get()==('Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State') and Destination.get()==('Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State'):
    #     price=20000
    # elif Destination.get()==('Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State') and Boarding.get()==('Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State'):
    #     price=20000
    # elif Boarding.get()==('Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State') and Destination.get()==('Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT'):
    #     price=12000
    # elif Destination.get()==('Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State') and Boarding.get()==('Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT'):
    #     price=12000
    # #n_east
    # elif Boarding.get()==('Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State') and Destination.get()==('Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State'):
    #     price=5500
    # elif Destination.get()==('Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State') and Boarding.get()==('Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State'):
    #     price=5500
    # elif Boarding.get()==('Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State') and Destination.get()==('Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT'):
    #     price=5000
    # elif Destination.get()==('Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State') and Boarding.get()==('Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT'):
    #     price=5000
    # #n_west
    # elif Boarding.get()==('Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State') and Destination.get()==('Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT'):
    #     price=5000
    # elif Destination.get()==('Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State') and Boarding.get()==('Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT'):
    #     price=5000
        
    else:
        print("me")
    
   
    # for i in s_west:
    #     print(i)
    #     pass
    # for j in s_east:
    #     print(j)
    #     pass
    #s_west to all
    

    # if Boarding.get()==()
    # total=price * (int(Passengerno.get()))
    # total_price=f'₦{total}'
    # print(total_price)
    
    # no_passenger2.configure(text=Passengerno.get())
    # from2.configure(text=Boarding.get())
    # to2.configure(text=Destination.get())
    # tCost2.configure(text=total_price)
    # dbQuery = db.controller()
    
    # if((Busno.get()) == "" or (Boarding.get()) == "" or (Destination.get())== "" or (Busstop.get())== "" or (Passengerno.get())== ""):
    #     messagebox.showwarning('Empyt Field', 'The field is required please fill.')
    #     return
    # # print(Busno.get())
    # # values=((Busno.get()),(Boarding.get()),(Destination.get()),(Busstop.get()),(Passengerno.get()))
    # # print(values)
    # try:
    #     sql = "INSERT INTO `book`(`bus_no`, `boarding`, `destination`, `bus_stop`, `passenger_no`,`Ticket_no`) VALUES (%s,%s,%s,%s,%s,%s)"
    #     print("i dey here")
        
    #     values=((Busno.get()),(Boarding.get()),(Destination.get()),(Busstop.get()),(Passengerno.get()),Ticketno.get())
    #     print("i dey here")
    #     print(values)
    #     dbQuery.queryDB(sql,values)

    #     messagebox.showinfo('Saved Record', 'Record has been saved successfully.')
    #     Busno.set("")
    #     Boarding.set("")
    #     Destination.set("")
    #     Busstop.set("")
    #     Passengerno.set("")
    #     # Ticketno.set("")
    # except:
    #     messagebox.showerror("err", "Record not successfully saved")
    
def exiT():
    pass
def reseT():
    pass
def travel_Cost():
    pass
def bus_Stops(self):
        des_bb_Combo['values'] = bus_stops[des_Combo.get()]




bus_no=['A1001','A1002','A1003','A1004','A1005','A1006','A1007','A1008','A1009','A1010','A1011','A1012']

bus_stops = {'Abia State':['Umuahia','Aba','Arochukwu'],
'Adamawa State': ['Jimeta','Mubi','Numan','Yola'],
'Akwa Ibom State': ['Ikot Abasi','Ikot Ekpene','Oron','Uyo'],
'Anambra State': ['Awka','Onitsha'],
'Bauchi State': ['Azare','Bauchi',"Jama′are"'Katagum','Misau'],
'Bayelsa State': ['Brass','Yenagoa'],
'Benue State': ['Makurdi'],
'Borno State': ['Biu','Dikwa','Maiduguri'],
'Cross River State':['Calabar','Ogoja'],
'Delta State': ['Asaba','Burutu','Koko','Sapele','Ughelli','Warri'],
'Ebonyi State ': ['Abakaliki'],
'Edo State': ['Benin City'],
'Ekiti State': ['Ado-Ekiti','Effon-Alaiye','Ikere-Ekiti'],
'Enugu State': ['Enugu','Nsukka'],
'FCT':['Abuja'],
'Gombe State': ['Deba', 'Habe''Gombe'],
'Imo State':['Owerri'],
'Jigawa State': ['Birnin Kudu','Dutse','Hadejia'],
'Kaduna State': ['Jemaa','Kaduna','Zaria'],
'Kano State':['Kano'],
'Katsina State' :['Daura','Katsina'],
'Kebbi State': ['Argungu','Birnin Kebbi','Yelwa'],
'Kogi State': ['Kabba','Lokoja','Okene'],
'Kwara State': ['Ilorin','Jebba','Lafiagi','Offa'],
'Lagos State':['Berger','Ikeja','Ikorodu','Lagos','Mushin','Oshodi'],
'Nasarawa State':['Keffi','Lafia','Nasarawa'],
'Niger State':['Bida','Lapai','Lokoja','Minna','Suleja'],
'Ogun State ':['Abeokuta','Ijebu-Ode','Ilaro','Shagamu'],
'Ondo State': ['Akure','Ikare','Oka-Akoko','Ondo','Owo'],
'Osun State': ['Ede','Ile-Ife','Ilesha','Iwo','Oshogbo'],
'Oyo State':['Ibadan','Iseyin','Ogbomosho','Oyo','Saki'],
'Plateau State':['Jos','Vom','Wase'],
'Rivers State': ['Bonny','Degema','Okrika','Port Harcourt'],
'Sokoto State':['Sokoto'],
'Taraba State':['Ibi','Jalingo','Muri'],
'Yobe State': ['Damaturu','Nguru'],
'Zamfara State':['Gusau','Kaura Namoda']
}

rt =ThemedTk(theme='adapta', themebg=True)
rt.title("JayTeeOjo Transportation")
width = 732
height = 443
sw = rt.winfo_screenwidth()
sh = rt.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
rt.geometry(f'{width}x{height}+{x}+{y}')
rt.resizable(0, 0)

style = ttk.Style()
style.configure("textlbl.TLabel", font=("Arial",14,"bold"))
style.configure("textlbl.TEntry", font=("Arial",14,"bold"))

Date1 = StringVar()
now = dt.datetime.now()
Date1.set(now.strftime("%d-%m-%Y  %I:%M:%S:%p"))

frame_Booking_Panel = ttk.Frame(rt)
frame_Booking_Panel.place(x=0, y=0, relheight=1, relwidth=1)

img=Image.open("img/bus_blur2.png")
imgsize=img.resize((732,443))
imgtp= ImageTk.PhotoImage(imgsize) 
LogoLabel = ttk.Label(frame_Booking_Panel,image=imgtp)
LogoLabel.place(x=1,y=0,relheight=1,relwidth=1) 

#stringvar
Ticketno=StringVar()
Busno=StringVar()
Boarding=StringVar()
Destination=StringVar()
Busstop=StringVar()
Passengerno=StringVar()

ticket_no= ttk.Label(frame_Booking_Panel,text="Ticket No: ",style="textlbl.TLabel")
ticket_no.place(relx=0.01, rely=0.08, height=30, width=120)

ticket_entry=ttk.Entry(frame_Booking_Panel,textvariable=Ticketno,font=("Arial",14,"bold"))
ticket_entry.place(relx=0.19, rely=0.08, height=30, width=145)

Bus_No = ttk.Label(frame_Booking_Panel,text="  Bus No  : ",style="textlbl.TLabel")
Bus_No.place(relx=0.01, rely=0.18, height=24, width=120)

busno_Combo = ttk.Combobox(frame_Booking_Panel, state='readonly',values=bus_no,textvariable=Busno,font=("Arial",10,"bold"))
busno_Combo.place(relx=0.19, rely=0.18, relheight=0.05, relwidth=0.2)
# busno_Combo.set("Select Number")



boarding_lbl = ttk.Label(frame_Booking_Panel,text="Boarding :",style="textlbl.TLabel")
boarding_lbl.place(relx=0.01, rely=0.32, height=23, width=120)
# boarding_lbl.configure(background="#ff0080")


destination_lbl = ttk.Label(frame_Booking_Panel,text="Destination :",style="textlbl.TLabel")
destination_lbl.place(relx=0.52, rely=0.32, height=21, width=134)
# destination_lbl.configure(background="#ff0080")



boarding_Combo = ttk.Combobox(frame_Booking_Panel, state='readonly',values=list(bus_stops.keys()),textvariable=Boarding,font=("Arial",10,"bold"))
boarding_Combo.place(relx=0.19, rely=0.32, relheight=0.05, relwidth=0.2)
# boarding_Combo.set("Select Boarding")



des_Combo = ttk.Combobox(frame_Booking_Panel, state='readonly',values=list(bus_stops.keys()),textvariable=Destination,font=("Arial",10,"bold"))
des_Combo.place(relx=0.74, rely=0.32, relheight=0.05, relwidth=0.2)
# des_Combo.set("Select Destination")
des_Combo.bind('<<ComboboxSelected>>',bus_Stops)

des_bb_Combo = ttk.Combobox(frame_Booking_Panel, state='readonly',textvariable=Busstop,font=("Arial",10,"bold"))
des_bb_Combo .place(relx=0.74, rely=0.39, relheight=0.05, relwidth=0.2)
des_bb_Combo .bind('<<ComboboxSelected>>')
# des_bb_Combo .set("Select Bus Stop")

passengers_lbl = ttk.Label(frame_Booking_Panel)
passengers_lbl.place(relx=0.01, rely=0.47, height=23, width=120)
# passengers_lbl.configure(background="#7d0d82")
passengers_lbl.configure(font=(10))
passengers_lbl.configure(text="Passenger(s) :")

no_of_passenger = ttk.Combobox(frame_Booking_Panel, state='readonly',textvariable=Passengerno,font=("Arial",10,"bold"))
no_of_passenger.place(relx=0.19, rely=0.47, relheight=0.05, relwidth=0.15)
no_of_passenger['values'] = ("1", "2", "3")                                     #here
# no_of_passenger.set("Select Number")
no_of_passenger.bind('<<ComboboxSelected>>')

# no_of_Child = ttk.Combobox(frame_Booking_Panel, state='readonly')
# no_of_Child.place(relx=0.16, rely=0.65, relheight=0.05, relwidth=0.15)
# no_of_Child['values'] = ("0", "1", "2", "3")
# no_of_Child.set("Select Child(s)")
# no_of_Child.bind('<<ComboboxSelected>>')

total_Button = Button(frame_Booking_Panel)
total_Button.place(relx=0.18, rely=0.92, height=24, width=107)
# total_Button.configure(background="#008040")
total_Button.configure(font=(10))
total_Button.configure(text="Total")
total_Button.configure(command=travel_Cost)

book_Button = Button(frame_Booking_Panel)
book_Button.place(relx=0.38, rely=0.92, height=24, width=107)
# book_Button.configure(background="#008040")
book_Button.configure(font=(10))
book_Button.configure(text="Book")
book_Button.configure(command=booked)


reset_Button = Button(frame_Booking_Panel)
reset_Button.place(relx=0.58, rely=0.92, height=24, width=107)
# reset_Button.configure(background="#008040")
reset_Button.configure(font=(10))
reset_Button.configure(text="Reset")
reset_Button.configure(command=reseT)


exit_Button = Button(frame_Booking_Panel)
exit_Button.place(relx=0.78, rely=0.92, height=24, width=107)
# exit_Button.configure(background="#008040")
exit_Button.configure(font=(10))
exit_Button.configure(text="Exit")
exit_Button.configure(command=exiT)

# lblAdultno = Label(frame_Booking_Panel)
# lblAdultno.place(relx=0.05, rely=0.56, height=21, width=64)
# # lblAdultno.configure(background="#ff8040")
# lblAdultno.configure(text="Adult")

# lblChildno = Label(frame_Booking_Panel)
# lblChildno.place(relx=0.05, rely=0.65, height=21, width=64)
# # lblChildno.configure(background="#ff8040")
# lblChildno.configure(text="Child")

total_Frame = Frame(frame_Booking_Panel)
total_Frame.place(relx=0.36, rely=0.53, relheight=0.38, relwidth=0.36)
total_Frame.configure(relief=GROOVE)
total_Frame.configure(borderwidth="1")
# total_Frame.configure(background="#808080")

from1 = Label(total_Frame)
from1.place(relx=0.08, rely=0.09, height=21, width=54)
# from1.configure(background="#0080ff")
from1.configure(text="From :")

from2 = Label(total_Frame)
from2.place(relx=0.40, rely=0.09, height=21, width=121)
# from2.configure(background="#8080ff")
from2.configure(highlightcolor="black")

to1 = Label(total_Frame)
to1.place(relx=0.08, rely=0.27, height=21, width=49)
# to1.configure(background="#0080ff")
to1.configure(text="To :")

to2 = Label(total_Frame)
to2.place(relx=0.40, rely=0.27, height=21, width=121)
# to2.configure(background="#8080ff")

no_passenger = Label(total_Frame,text="Passenger(s):")
no_passenger.place(relx=0.08, rely=0.47, height=21, width=70)
# no_of_Adults1.configure(background="#0080ff")


no_passenger2 = Label(total_Frame)
no_passenger2.place(relx=0.40, rely=0.47, height=21, width=121)

#cost box
tCost1 = Label(total_Frame,text="Total Cost")
tCost1.place(relx=0.08, rely=0.67, height=21, width=74)

tCost2 = Label(total_Frame)
tCost2.place(relx=0.40, rely=0.67, height=21, width=121)
# tCost2.configure(background="#8080ff")




lbltiming1 = Label(total_Frame)
lbltiming1.place(relx=0.08, rely=0.82, height=21, width=74)
# lbltiming1.configure(background="#0080ff")
lbltiming1.configure(text="Booking at :")

lbltiming2 = Label(total_Frame)
lbltiming2.place(relx=0.40, rely=0.82, height=21, width=135)
# lbltiming2.configure(background="#8080ff")
lbltiming2.configure(textvariable=Date1)




lts=string.ascii_lowercase
letters=''.join(random.sample(lts,2))
num=string.digits
num2=100
number="".join(random.sample(num,4))
code=str(num2)+str(number)+str(letters)
Ticketno.set(code)


rt.mainloop()