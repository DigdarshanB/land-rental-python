import datetime

def display_available_lands(lands):
    """This function displays available lands from the text file"""
    print("Available Lands:\n")
    print("Kitta No.\tCity/District\tDirection\tArea\tPrice\tStatus")
    for land in lands:
        if land['status'] == 'Available':
            print(f"{land['kitta_number']}\t\t{land['city']}\t\t{land['direction']}\t\t{land['area']}\t\t{land['price']}\t\t{land['status']}")


def rent_land(lands, customer_name, duration):
    """Description of the function:
    -lands, customer_name and duration are taken as the parameters
    -Available lands are shown and you need to input kitta number of the land
    -Land gets rented and you have the option to continue or stop
    -Invoice is generated
    """
    rented_lands = []
    total_amount = 0
    print("Available Lands:\n")
    print("Kitta No.\tCity/District\tDirection\tArea\tPrice\tStatus\n")
    for land in lands:
        if land['status'] == 'Available':
            print(f"{land['kitta_number']}\t\t{land['city']}\t\t{land['direction']}\t\t{land['area']}\t\t{land['price']}\t\t{land['status']}\n")
    while True:
        kitta_number = input("Enter the kitta number of the land you want to rent (or type 'exit' to cancel): ")
        if kitta_number.lower() == 'exit':
            break
        else:
            for land in lands:
                if land['kitta_number'] == int(kitta_number) and land['status'] == 'Available':
                    rented_duration = duration
                    current_datetime = datetime.datetime.now()
                    rent_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                    total_amount +=  rented_duration * land['price'] # (a+=b == a+b, a+=b+c == a+b+c)
                    land['status'] = 'Not Available'
                    land['rent_date'] = rent_datetime 
                    rented_lands.append(land)
                    print(f"Land with kitta number {kitta_number} rented successfully.")
                    more_lands = input("Do you want to rent more land? (yes/no): ")
                    if more_lands.lower() == 'no':
                        techno_prop_invoice_name = f"Rent_Invoice_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
                        with open(techno_prop_invoice_name, 'w') as techno_prop_invoice:
                            techno_prop_invoice.write("Rent Invoice\n\n")
                            techno_prop_invoice.write(f"Customer Name: {customer_name}\n")
                            techno_prop_invoice.write(f"Date and Time of Rent: {rent_datetime}\n")
                            techno_prop_invoice.write("Rented Lands:\n")
                            for land in rented_lands:
                                techno_prop_invoice.write(f"- Kitta Number: {land['kitta_number']}\n")
                                techno_prop_invoice.write(f"  City/District: {land['city']}\n")
                                techno_prop_invoice.write(f"  Direction: {land['direction']}\n")
                                techno_prop_invoice.write(f"  Area: {land['area']} anna\n")
                            techno_prop_invoice.write(f"Total Amount: {total_amount}\n")
                        print("Invoice generated!")
                        return
                    elif more_lands.lower() == 'yes':
                        break
            else:
                print("Invalid kitta number. Please try again.")


def return_land(lands):
    """Description of the function:
    -lands is taken as the parameter
    -rented lands are shown
    -input for land to be returned is asked and land is returned
    -total amount is calculated and invoice is generated
    -fine is added if land is returned late and invoice with total amount is generated
    """
    returned_lands = []
    total_amount = 0
    total_fine = 0
    print("Rented Lands:")
    print("Kitta No.\tCity/District\tDirection\tArea\tPrice\tStatus")
    for land in lands:
        if land['status'] == 'Not Available':
            print(f"{land['kitta_number']}\t\t{land['city']}\t\t{land['direction']}\t\t{land['area']}\t\t{land['price']}\t\t{land['status']}")
    while True:
        kitta_number = input("Enter the kitta number of the land you want to return (or type 'exit' to cancel): ")
        if kitta_number.lower() == 'exit':
            break
        else:
            found_land = False
            for land in lands:
                if land['kitta_number'] == int(kitta_number):
                    found_land = True
                    if land['status'] == 'Not Available':
                        current_datetime = datetime.datetime.now()
                        return_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                        rent_datetime = land.get('rent_date')
                        if rent_datetime: 
                            rent_date = datetime.datetime.strptime(rent_datetime, '%Y-%m-%d %H:%M:%S')
                            rented_duration = (current_datetime.year - rent_date.year) * 12 + current_datetime.month - rent_date.month
                            if rented_duration < 1:
                                rented_duration = 1 
                            fine_months = (current_datetime.year - rent_date.year) * 12 + current_datetime.month - rent_date.month - rented_duration
                            if fine_months > 0:
                                fine_price = 0.1 * fine_months * land['price']
                                total_fine += fine_price
                            total_amount += rented_duration * land['price']
                            returned_lands.append(land)
                        land['status'] = 'Available' 
                        print(f"Land with kitta number {kitta_number} returned successfully.")
                        techno_prop_invoice_name = f"Return_Invoice_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
                        with open(techno_prop_invoice_name, 'w') as techno_prop_invoice:
                            techno_prop_invoice.write("Return Invoice\n\n")
                            techno_prop_invoice.write(f"Date and Time of Return: {return_datetime}\n")
                            techno_prop_invoice.write("Returned Lands:\n")
                            for land in returned_lands:
                                techno_prop_invoice.write(f"- Kitta Number: {land['kitta_number']}\n")
                                techno_prop_invoice.write(f"  City/District: {land['city']}\n")
                                techno_prop_invoice.write(f"  Direction: {land['direction']}\n")
                                techno_prop_invoice.write(f"  Area: {land['area']} anna\n")
                            techno_prop_invoice.write(f"Total Amount: {total_amount}\n")
                            if total_fine > 0:
                                techno_prop_invoice.write(f"Late Return Fine: {total_fine}\n")
                                techno_prop_invoice.write(f"Amount with Fine: {total_amount + total_fine}\n")
                        print("Invoice generated!")
                        return
                    else:
                        print("This land was never rented.")
                        land['status'] = 'Available'
                        return
            if not found_land:
                print("This land does not exist in the system.")
                return

