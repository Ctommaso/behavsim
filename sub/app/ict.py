import random as rd
import numpy as np
import sub.gui
import sub.rd_var
import time


# Defines the ict function.
def ict(param, res_dir, text_view):
    
    # Defines the number of minutes in a day
    mins = 1440
    
    # Defines the name of the appliance.
    name = "ICT"
        
    # Starts a timer.
    start_global_time = time.time()
    
    # Writes intro to terminal.
    sub.gui.display(text_view, "New "+name+" Consumption Simulation!", "red")
    
    # Repeats the following for each house.
    for i in range(int(round(param["Number of Houses"][0]))):
        
        # Starts a timer.
        start_local_time = time.time()
        
        # Initializes the active power vector.
        active_power = np.zeros(mins*param["Number of Days"][0])
        
        # Repeats the following for each day.
        for j in range(int(round(param["Number of Days"][0]))):
            
            # Continues only if the day is a week day.
            if j % 7 != 5 and j % 7 != 6:

                # Computes a breakfast use if prob is OK.
                if 100*rd.random() <= param["Morning Prob [%]"][0]:
                    l1 = mins*j+sub.rd_var.norm(param["Morning Time [hour]"][0]*60,
                                                param["Morning Time [hour]"][1]*60,
                                                True)
                    l2 = l1+sub.rd_var.norm(param["Morning Duration [min]"][0],
                                            param["Morning Duration [min]"][1],
                                            True)
                    power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
                    active_power[l1:l2] += power

                # Computes a lunch use if prob is OK.
                if 100*rd.random() <= param["Afternoon Prob [%]"][0]:
                    l1 = mins*j+sub.rd_var.norm(param["Afternoon Time [hour]"][0]*60,
                                                param["Afternoon Time [hour]"][1]*60,
                                                True)
                    l2 = l1+sub.rd_var.norm(param["Afternoon Duration [min]"][0],
                                            param["Afternoon Duration [min]"][1],
                                            True)
                    power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
                    active_power[l1:l2] += power

                # Computes a dinner use if prob is OK.
                if 100*rd.random() <= param["Evening Prob [%]"][0]:
                    l1 = mins*j+sub.rd_var.norm(param["Evening Time [hour]"][0]*60,
                                                param["Evening Time [hour]"][1]*60,
                                                True)
                    l2 = l1+sub.rd_var.norm(param["Evening Duration [min]"][0],
                                            param["Evening Duration [min]"][1],
                                            True)
                    power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
                    active_power[l1:l2] += power

            # Continues only if the day is a weekend day.
            if j % 7 == 5 or j % 7 == 6:

                # Computes a breakfast use if prob is OK.
                if 100*rd.random() <= param["Morning Prob (WE) [%]"][0]:
                    l1 = mins*j+sub.rd_var.norm(param["Morning Time (WE) [hour]"][0]*60,
                                                param["Morning Time (WE) [hour]"][1]*60,
                                                True)
                    l2 = l1+sub.rd_var.norm(param["Morning Duration (WE) [min]"][0],
                                            param["Morning Duration (WE) [min]"][1],
                                            True)
                    power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
                    active_power[l1:l2] += power

                # Computes a lunch use if prob is OK.
                if 100*rd.random() <= param["Afternoon Prob (WE) [%]"][0]:
                    l1 = mins*j+sub.rd_var.norm(param["Afternoon Time (WE) [hour]"][0]*60,
                                                param["Afternoon Time (WE) [hour]"][1]*60,
                                                True)
                    l2 = l1+sub.rd_var.norm(param["Afternoon Duration (WE) [min]"][0],
                                            param["Afternoon Duration (WE) [min]"][1],
                                            True)
                    power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
                    active_power[l1:l2] += power

                # Computes a dinner use if prob is OK.
                if 100*rd.random() <= param["Evening Prob (WE) [%]"][0]:
                    l1 = mins*j+sub.rd_var.norm(param["Evening Time (WE) [hour]"][0]*60,
                                                param["Evening Time (WE) [hour]"][1]*60,
                                                True)
                    l2 = l1+sub.rd_var.norm(param["Evening Duration (WE) [min]"][0],
                                            param["Evening Duration (WE) [min]"][1],
                                            True)
                    power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
                    active_power[l1:l2] += power

        # Prapares the data to be saved in a .csv file.
        csv_data = map(list, zip(*[active_power]))

        # Defines and opens the .csv file.
        csv_file = res_dir+"/"+"house_%000006d.csv" % (i+1)
        fid_w = open(csv_file, "w")

        # Saves the data to the .csv file.
        np.savetxt(fid_w, csv_data, fmt="%.5e", delimiter=",")

        # Computes the daily average power.
        avg_power = sum(active_power)/param["Number of Days"][0]/60000

        # Computes the local simulation time.
        local_time = time.time()-start_local_time

        # Writes the house status to the terminal.
        text = "House %d:" % (i+1)
        sub.gui.display(text_view, text, "blue")
        text = "Daily average energy = %.3f kWh." % avg_power
        sub.gui.display(text_view, text, "white")
        text = "Duration = %.3f seconds." % local_time
        sub.gui.display(text_view, text, "white")

    # Computes the global simulation time.
    gt = time.time()-start_global_time
    h = int(gt//3600.0)
    m = int((gt % 3600.0)//60.0)
    s = (gt % 3600.0) % 60.0

    # Writes the global simulation time to the terminal.
    text = "The "+name+" Consumption Simulation took:"
    sub.gui.display(text_view, text, "red")
    
    text = "%d hours, %d minutes, and %.3f seconds." % (h, m, s)
    sub.gui.display(text_view, text, "red")
