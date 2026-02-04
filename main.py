'''
This is the main file for the turntable azimuth readout and 
calculation. Defines event handler and displays messages for
user.
'''

# Imports packages
from datetime import datetime
from gpiozero import Button
from signal import pause

# Defines function for button closing
def on_close():
    '''
    This function is the handler for the event when the
    button closes. Displays message that circuit is
    closed.
    '''
    # Creates timestamp
    dt_now_str = str(datetime.now())

    # Creates entry to be written
    line = dt_now_str + '\n'
    
    # Writes to file
    file.write(line)

    # Displays message for user
    print(f"Circuit closed (pin pulled to GND) at {dt_now_str}")

# Main program
if __name__ == "__main__":

    # Creates start date time string
    start_dt_str = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

    # Creates Button instance using GPIO17
    button = Button(17, pull_up=True, bounce_time = 0.1)
    
    # Assigns event handler function
    button.when_pressed = on_close

    # Displays program start and user prompt
    print("Start of azimuth timestamp logging.")
    print("Monitoring GPIO17.")
    print("Toggle your switch. Ctrl+C to exit.\n")

    # Starts exception handling suites for signal event loop
    try:
        # Creates file access object
        file = open(f"../data/az_log_{start_dt_str}.txt", "w")
        # Starts signal event handling loop
        pause()

    except:
        # Displays message informing user of action
        print("User initiated end of program.")
    
    finally:
        # Closes file access regardless of runtime error
        file.close()

        # Displays message for end of program
        print("End of azimuth timestamp logging.")

