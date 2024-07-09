from read import read_land_data
from write import write_land_data
from operations import display_available_lands, rent_land, return_land

def main():
    """Description of the function:
    -Reads the textfile
    -available lands are displayed by calling the function from operations.py file
    -3 choices are given and user input is requested
    -choosing 1 leads to renting lands
    -choosing 2 leads to returning lands
    -choosing 3 exits the program

    """
    file_name = "land_info.txt"
    lands = read_land_data(file_name)
    while True:
        print("----------------TechnoPropertyNepal----------------- \n")
        print("\t\tSanothimi, Bhaktapur\n")
        print("\t\tContact: 9843887532")
        print("----------------------------------------------------\n\n")
        display_available_lands(lands)
        print("\nMenu:")
        print("1. Rent Land")
        print("2. Return Land")
        print("3. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                customer_name = input("Enter customer name: ")
                duration = int(input("Enter duration of rent (in months): "))
                #After entering name and duration of rent, rent_land function from operations is called.
                rent_land(lands, customer_name, duration)
            elif choice == '2':
                #return_land function is called if 2 is selected.
                return_land(lands)
            elif choice == '3':
                write_land_data(file_name, lands)
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
