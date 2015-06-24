#!/usr/bin/env python

import sub.gui
import gtk


# Defines the main function.
def main():
    
    # Starts GTK.
    gtk.main()

# Executes the following only if behav_sim.py is directly executed.
if __name__ == "__main__":
    
    # Creates an instance of the Simulator class.
    simulator = sub.gui.Simulator()
    
    # Calls main function.
    main()
