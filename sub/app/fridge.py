import random as rd
import numpy as np
import sub.gui
import sub.rd_var
import time
import math


# Defines the fridge function.
def fridge(param, res_dir, text_view):
    
    # Defines the number of minutes in a day.
    mins = 1440
    
    # Defines the name of the appliance.
    name = "Fridge"
    
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
        
        # Computes the parameters of the first period.
        on = sub.rd_var.norm(param["Compressor On [min]"][0], param["Compressor On [min]"][1], True)
        off = sub.rd_var.norm(param["Compressor Off [min]"][0], param["Compressor Off [min]"][1], True)
        power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
        peak_power = sub.rd_var.norm(param["Power [W]"][0]/2.0, param["Power [W]"][0]/2.0, False, trunc_neg=-1,
                                     trunc_pos=1)
        
        # Computes the first period.
        tmp_power = np.zeros(on+off)
        tmp_power[0:on] = power
        for j in range(on):
            tmp_power[j] += peak_power*math.exp(-j)
            
        # Select initial point.
        start = sub.rd_var.uni(0, on+off, True)
        tmp_power = tmp_power[start:]
        
        # Adds the initial period.
        l1 = 0
        l2 = len(tmp_power)
        active_power[l1:l2] += tmp_power
        
        # Repeats the following until the end of the time vector.
        skip = False
        while l2 < mins*param["Number of Days"][0]:
            
            # Computes the parameters of the period.
            on = sub.rd_var.norm(param["Compressor On [min]"][0], param["Compressor On [min]"][1], True)
            off = sub.rd_var.norm(param["Compressor Off [min]"][0], param["Compressor Off [min]"][1], True)
            power = sub.rd_var.norm(param["Power [W]"][0], param["Power [W]"][1], False)
            peak_power = sub.rd_var.norm(param["Power [W]"][0]/2.0, param["Power [W]"][0]/2.0, False, trunc_neg=-1,
                                         trunc_pos=1)
            if skip:
                on += on
                skip = False
             
            # Computes and adds the period.
            tmp_power = np.zeros(on+off)
            tmp_power[0:on] = power
            for j in range(on):
                tmp_power[j] += peak_power*math.exp(-j)
            l1 = l2
            l2 = min(l1+len(tmp_power), mins*param["Number of Days"][0])
            if 100*rd.random() <= param["Cycle Probability [%]"][0]:
                active_power[l1:l2] += tmp_power[:l2-l1]
            else:
                skip = True

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
