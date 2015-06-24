import random as rd
import numpy as np
import sub.gui
import sub.rd_var
import time
import math


# Defines the stove function.
def stove(param, res_dir, text_view):
    
    # Defines the number of minutes in a day
    mins = 1440
    
    # Defines the name of the appliance.
    name = "Stove"
        
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
                if 100*rd.random() <= param["Breakfast Prob [%]"][0]:
                    l1 = mins*j+sub.rd_var.norm(param["Breakfast Time [hour]"][0]*60,
                                                param["Breakfast Time [hour]"][1]*60,
                                                True)
                    l2 = l1+sub.rd_var.norm(param["Breakfast Duration [min]"][0],
                                            param["Breakfast Duration [min]"][1],
                                            True)
                    l2 = min(l2, mins*param["Number of Days"][0])
                    power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
                    if param["Induction?"][0] == "Yes":
                        tmp_power = power*np.ones(l2-l1)
                        for k in range(l2-l1):
                            tmp_power[k] += power*math.exp(-0.5*k)/20.0
                        active_power[l1:l2] += tmp_power
                    else:
                        active_power[l1:l2] += power
                    
                # Computes a lunch use if prob is OK.
                if 100*rd.random() <= param["Lunch Prob [%]"][0]:
                    l1 = mins*j+sub.rd_var.norm(param["Lunch Time [hour]"][0]*60,
                                                param["Lunch Time [hour]"][1]*60,
                                                True)
                    l2 = l1+sub.rd_var.norm(param["Lunch Duration [min]"][0],
                                            param["Lunch Duration [min]"][1],
                                            True)
                    l2 = min(l2, mins*param["Number of Days"][0])
                    power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
                    if param["Induction?"][0] == "Yes":
                        tmp_power = power*np.ones(l2-l1)
                        for k in range(l2-l1):
                            tmp_power[k] += power*math.exp(-0.5*k)/20.0
                        active_power[l1:l2] += tmp_power
                    else:
                        active_power[l1:l2] += power
                    
                # Computes a dinner use if prob is OK.
                if 100*rd.random() <= param["Dinner Prob [%]"][0]:
                    l1 = mins*j+sub.rd_var.norm(param["Dinner Time [hour]"][0]*60,
                                                param["Dinner Time [hour]"][1]*60,
                                                True)
                    l2 = l1+sub.rd_var.norm(param["Dinner Duration [min]"][0],
                                            param["Dinner Duration [min]"][1],
                                            True)
                    l2 = min(l2, mins*param["Number of Days"][0])
                    power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
                    if param["Induction?"][0] == "Yes":
                        tmp_power = power*np.ones(l2-l1)
                        for k in range(l2-l1):
                            tmp_power[k] += power*math.exp(-0.5*k)/20.0
                        active_power[l1:l2] += tmp_power
                    else:
                        active_power[l1:l2] += power
                    
            # Continues only if the day is a weekend day.
            if j % 7 == 5 or j % 7 == 6:
                
                # Computes a breakfast use if prob is OK.
                if 100*rd.random() <= param["Breakfast Prob (WE) [%]"][0]:
                    l1 = mins*j+sub.rd_var.norm(param["Breakfast Time (WE) [hour]"][0]*60,
                                                param["Breakfast Time (WE) [hour]"][1]*60,
                                                True)
                    l2 = l1+sub.rd_var.norm(param["Breakfast Duration (WE) [min]"][0],
                                            param["Breakfast Duration (WE) [min]"][1],
                                            True)
                    l2 = min(l2, mins*param["Number of Days"][0])
                    power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
                    if param["Induction?"][0] == "Yes":
                        tmp_power = power*np.ones(l2-l1)
                        for k in range(l2-l1):
                            tmp_power[k] += power*math.exp(-0.5*k)/20.0
                        active_power[l1:l2] += tmp_power
                    else:
                        active_power[l1:l2] += power

                # Computes a lunch use if prob is OK.
                if 100*rd.random() <= param["Lunch Prob (WE) [%]"][0]:
                    l1 = mins*j+sub.rd_var.norm(param["Lunch Time (WE) [hour]"][0]*60,
                                                param["Lunch Time (WE) [hour]"][1]*60,
                                                True)
                    l2 = l1+sub.rd_var.norm(param["Lunch Duration (WE) [min]"][0],
                                            param["Lunch Duration (WE) [min]"][1],
                                            True)
                    l2 = min(l2, mins*param["Number of Days"][0])
                    power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
                    if param["Induction?"][0] == "Yes":
                        tmp_power = power*np.ones(l2-l1)
                        for k in range(l2-l1):
                            tmp_power[k] += power*math.exp(-0.5*k)/20.0
                        active_power[l1:l2] += tmp_power
                    else:
                        active_power[l1:l2] += power

                # Computes a dinner use if prob is OK.
                if 100*rd.random() <= param["Dinner Prob (WE) [%]"][0]:
                    l1 = mins*j+sub.rd_var.norm(param["Dinner Time (WE) [hour]"][0]*60,
                                                param["Dinner Time (WE) [hour]"][1]*60,
                                                True)
                    l2 = l1+sub.rd_var.norm(param["Dinner Duration (WE) [min]"][0],
                                            param["Dinner Duration (WE) [min]"][1],
                                            True)
                    l2 = min(l2, mins*param["Number of Days"][0])
                    power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
                    if param["Induction?"][0] == "Yes":
                        tmp_power = power*np.ones(l2-l1)
                        for k in range(l2-l1):
                            tmp_power[k] += power*math.exp(-0.5*k)/20.0
                        active_power[l1:l2] += tmp_power
                    else:
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
    text = "The "+name+" Consumption Simulation took %d hours, %d minutes, and %.3f seconds." % (h, m, s)
    sub.gui.display(text_view, text, "red")
