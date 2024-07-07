def read_land_data(file_name):
    """
    This function reads the text file and returns a list of dictionary
    that contains information about lands. 
    """
    
    land_data = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                land = line.strip().split(',')
                land_data.append({
                    'kitta_number': int(land[0]),
                    'city': land[1].strip(),
                    'direction': land[2].strip(),
                    'area': int(land[3]),
                    'price': int(land[4]),
                    'status': land[5].strip()
                })
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f" An error occurred: {str(e)}")
    return land_data
