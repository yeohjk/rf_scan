'''
This file is for the processing of the logged azimuth data for
computing the azimuth angle at a specific date and time.
'''

# Imports packages
from datetime import datetime

# Defines function to extract data from file
def extract(file_name):
    '''
    This function extracts and transforms logged azimuth data to
    datetime objects. It takes the logged azimuth data file name
    as input. The raw data strings are converted to datetime objects.
    A list of the datetime objects is then returned.
    '''
    
    # Creates empty datetime list
    dt_list = []

    # Creates constant datetime parsing format
    FORMAT_STR = '%Y-%m-%d %H:%M:%S.%f'

    # Opens file based on argument
    with open(f"../rf_scan_gnuradio/data/{file_name}", "r") as file:
        # Extracts lines of date time string to a list
        content_list = file.readlines()
        
        # Loops through content list for transformation
        for line in content_list:
            # Transforms raw data string to datetime object
            dt_str = line.strip()
            dt_obj = datetime.strptime(dt_str, FORMAT_STR)
            
            # Appends datetime object to datetime list
            dt_list.append(dt_obj)
    
    return dt_list

# Defines function to calculate azimuth angle (degrees) for date and time
def azimuth(dt):
    '''
    This function calculates azimuth angle (degrees) for specific
    date and time using interpolation of logged azimuth data.
    '''
    return

# Main body of script
if __name__ == "__main__":
    # Prompt user for input of raw data file name
    file_name = input("Please input name of logged azimuth data file: ")
    # Extract out raw data and transform into list of datetime objects
    dt_list = extract(file_name)
    # Displays the number of entries
    print(f"Number of Entries: {len(dt_list)}")
