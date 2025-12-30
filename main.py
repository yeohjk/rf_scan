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
    print("Circuit closed (pin pulled to GND)")

# Main program
if __name__ == "__main__":

    # Creates Button instance using GPIO17
    button = Button(17, pull_up=True, bounce_time = 0.05)
    
    # Assigns event handler function
    button.when_pressed = on_close

    # Displays program state and user prompt
    print("Monitoring GPIO17.")
    print("Toggle your switch. Ctrl+C to exit.")

    # Starts signal event handling loop
    pause()