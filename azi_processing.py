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
def azimuth(dt, dt_list):
    '''
    This function calculates azimuth angle (degrees) for specific
    date and time using interpolation of logged azimuth data.
    '''
    # Instantiates index
    ind = 0
    
    # Loops through every datetime stamp in datetime list
    while True:
        # Assigns end_time to particular entry
        end_time = dt_list[ind]
        # Checks for dt being inside a time interval
        if dt <= end_time:
            # Assigns start_time to particular entry
            start_time = dt_list[ind - 1]
            # Calculates azimuth interval duration in seconds
            interval_time = (end_time - start_time).total_seconds()
            # Calculates time elapsed in seconds for position
            time_seconds = (dt - start_time).total_seconds()
            # Interpolates for azimuth angle
            azi_ang = (time_seconds/interval_time) * 360
            # For the case of angle = 360 degrees
            if azi_ang == 360:
                azi_ang = 0.00
            break
        # Increase index value by one
        ind += 1
    return azi_ang

# Defines function to format input string into datetime object
def dt_from_time_str(input_str, dt_ref):
    '''
    This function formats the user provided input string into a
    datetime object. It takes in the input string and a datetime
    object as reference for the date. The datetime object with the
    reference date and input string time is returned.
    '''
    # Creates constant time parsing format
    FORMAT_STR = '%H:%M:%S.%f'

    # Converts string to time object
    dt_input = datetime.strptime(input_str, FORMAT_STR).time()

    # Combines date from reference with parsed time
    new_datetime = datetime.combine(dt_ref.date(), dt_input)

    return new_datetime
    

# Main body of script
if __name__ == "__main__":
    # Prompts user for input of raw data file name
    file_name = input("Please input name of logged azimuth data file: ")
    # Extracts out raw data and transform into list of datetime objects
    dt_list = extract(file_name)
    # Displays the number of entries
    print(f"Number of entries in data file: {len(dt_list)}")

    # Prompts user for input of time of interest
    time_str = input("Please input time of interest (HH:MM:SS.ssssss): ")
    # Creates datetime object for time of interest
    dt_interest = dt_from_time_str(time_str, dt_list[0])
    # Calculates azimuth angle for time of interest
    azi_ang = azimuth(dt_interest, dt_list)
    # Displays azimuth angle
    print(f"Azimuth angle at {time_str}:\n{azi_ang:.2f}")
