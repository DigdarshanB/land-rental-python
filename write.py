def write_land_data(file_name, land_data):
    """
    -file_name and land_data are passed as parameters
    -file_name is opened in write mode and land data will be written to the file_name
    -handels exception which might occur during file handling
    """
    try:
        with open(file_name, 'w') as file:
            for land in land_data:
                file.write(f"{land['kitta_number']},{land['city']},{land['direction']},{land['area']},{land['price']},{land['status']}\n")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

