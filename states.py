# import bookings
# global Destination,Boarding
# def content():
#     global Destination,Boarding
#     price=""
#     s_west='Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State'
#     s_east='Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State'
#     s_south='Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State'
#     n_east='Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State'
#     n_west='Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State'
#     n_central='Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT'

# def stateprice():
#     #s_west
#     if bookings.Boarding.get()=='Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State' and bookings.Destination.get()=='Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State':
#         price=5000
#     elif Destination.get()=='Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State' and Boarding.get()=='Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State':
#         price=5000
#     elif Boarding.get()=='Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State' and Destination.get()=='Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State':
#         price=5500
#     elif Destination.get()=='Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State' and Boarding.get()=='Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State':
#         price=5500
#     elif Boarding.get()=='Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State' and Destination.get()=='Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State':
#         price=10500
#     elif Destination.get()=='Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State' and Boarding.get()=='Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State':
#         price=10500
#     elif Boarding.get()=='Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State' and Destination.get()=='Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State':
#         price=10000
#     elif Destination.get()=='Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State' and Boarding.get()=='Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State':
#         price=10000
#     elif Boarding.get()=='Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State' and Destination.get()=='Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT':
#         price=7000
#     elif Destination.get()=='Ondo State' or 'Osun State' or 'EKiti State' or 'Lagos State' or 'Ogun State' and Boarding.get()=='Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT':
#         price=7000
#     #s_east to all
#     elif Boarding.get()=='Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State' and Destination.get()=='Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State':
#         price=7000
#     elif Destination.get()=='Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State' and Boarding.get()=='Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State':
#         price=7000
#     elif Boarding.get()=='Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State' and Destination.get()=='Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State':
#         price=12000
#     elif Destination.get()=='Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State' and Boarding.get()=='Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State':
#         price=12000
#     elif Boarding.get()=='Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State' and Destination.get()=='Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State':
#         price=15000
#     elif Destination.get()=='Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State' and Boarding.get()=='Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State':
#         price=15000
#     elif Boarding.get()=='Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State' and Destination.get()=='Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT':
#         price=9000
#     elif Destination.get()=='Abia State' or 'Anambra State' or 'Ebonyi State' or 'Enugu State' or 'Imo State' and Boarding.get()=='Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT':
#         price=9000
#     #s_west
#     elif Boarding.get()=='Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State' and Destination.get()=='Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State':
#         price=20000
#     elif Destination.get()=='Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State' and Boarding.get()=='Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State':
#         price=20000
#     elif Boarding.get()=='Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State' and Destination.get()=='Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State':
#         price=20000
#     elif Destination.get()=='Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State' and Boarding.get()=='Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State':
#         price=20000
#     elif Boarding.get()=='Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State' and Destination.get()=='Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT':
#         price=12000
#     elif Destination.get()=='Akwa Ibom State' or 'Bayelsa State' or 'Cross River State' or 'Delta State' or 'Edo State' or 'Rivers State' and Boarding.get()=='Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT':
#         price=12000
#     #n_east
#     elif Boarding.get()=='Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State' and Destination.get()=='Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State':
#         price=5500
#     elif Destination.get()=='Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State' and Boarding.get()=='Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State':
#         price=5500
#     elif Boarding.get()=='Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State' and Destination.get()=='Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT':
#         price=5000
#     elif Destination.get()=='Adamawa State' or 'Bauchi State' or 'Borno State' or 'Gombe State' or 'Taraba State' or 'Yobe State' and Boarding.get()=='Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT':
#         price=5000
#     #n_west
#     elif Boarding.get()=='Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State' and Destination.get()=='Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT':
#         price=5000
#     elif Destination.get()=='Jigawa State' or 'Kaduna State' or 'Kano State' or 'Katsina State' or 'Kebbi State' or 'Sokoto State' or 'Zamfara State' and Boarding.get()=='Benue State' or 'Kogi State' or 'Kwara State' or 'Nasarawa State' or 'Niger State' or 'Plateau State' or 'FCT':
#         price=5000
        
#     else:
#         return
#     print(price)