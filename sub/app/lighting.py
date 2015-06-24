import numpy as np
import sub.gui
import sub.rd_var
import time


# Defines the lighting function.
def lighting(param, res_dir, text_view):
    
    # Defines the number of minutes in a day
    mins = 1440
    
    # Defines the name of the appliance.
    name = "Lighting"
        
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
                
                # Computes the morning bedrooms consumption.
                l1 = mins*j+sub.rd_var.norm(param["Bedrooms Morning Time [h]"][0]*60,
                                            param["Bedrooms Morning Time [h]"][1]*60,
                                            True)
                l2 = l1+sub.rd_var.norm(param["Bedrooms Morning Duration [min]"][0],
                                        param["Bedrooms Morning Duration [min]"][1],
                                        True)
                power = sub.rd_var.norm(param["Bedrooms Power [W]"][0], param["Bedrooms Power [W]"][1], False)
                active_power[l1:l2] += power
                    
                # Computes the evening bedrooms consumption.
                l1 = mins*j+sub.rd_var.norm(param["Bedrooms Evening Time [h]"][0]*60,
                                            param["Bedrooms Evening Time [h]"][1]*60,
                                            True)
                l2 = l1+sub.rd_var.norm(param["Bedrooms Evening Duration [min]"][0],
                                        param["Bedrooms Evening Duration [min]"][1],
                                        True)
                power = sub.rd_var.norm(param["Bedrooms Power [W]"][0], param["Bedrooms Power [W]"][1], False)
                active_power[l1:l2] += power
                    
                # Computes the morning bathrooms consumption.
                l1 = mins*j+sub.rd_var.norm(param["Bathrooms Morning Time [h]"][0]*60,
                                            param["Bathrooms Morning Time [h]"][1]*60,
                                            True)
                l2 = l1+sub.rd_var.norm(param["Bathrooms Morning Duration [min]"][0],
                                        param["Bathrooms Morning Duration [min]"][1],
                                        True)
                power = sub.rd_var.norm(param["Bathrooms Power [W]"][0], param["Bathrooms Power [W]"][1], False)
                active_power[l1:l2] += power
                    
                # Computes the evening bathrooms consumption.
                l1 = mins*j+sub.rd_var.norm(param["Bathrooms Evening Time [h]"][0]*60,
                                            param["Bathrooms Evening Time [h]"][1]*60,
                                            True)
                l2 = l1+sub.rd_var.norm(param["Bathrooms Evening Duration [min]"][0],
                                        param["Bathrooms Evening Duration [min]"][1],
                                        True)
                power = sub.rd_var.norm(param["Bathrooms Power [W]"][0], param["Bathrooms Power [W]"][1], False)
                active_power[l1:l2] += power
                    
                # Computes the morning kitchen consumption.
                l1 = mins*j+sub.rd_var.norm(param["Kitchen Morning Time [h]"][0]*60,
                                            param["Kitchen Morning Time [h]"][1]*60,
                                            True)
                l2 = l1+sub.rd_var.norm(param["Kitchen Morning Duration [min]"][0],
                                        param["Kitchen Morning Duration [min]"][1],
                                        True)
                power = sub.rd_var.norm(param["Kitchen Power [W]"][0], param["Kitchen Power [W]"][1], False)
                active_power[l1:l2] += power
                    
                # Computes the evening kitchen consumption.
                l1 = mins*j+sub.rd_var.norm(param["Kitchen Evening Time [h]"][0]*60,
                                            param["Kitchen Evening Time [h]"][1]*60,
                                            True)
                l2 = l1+sub.rd_var.norm(param["Kitchen Evening Duration [min]"][0],
                                        param["Kitchen Evening Duration [min]"][1],
                                        True)
                power = sub.rd_var.norm(param["Kitchen Power [W]"][0], param["Kitchen Power [W]"][1], False)
                active_power[l1:l2] += power

            # Continues only if the day is a weekend day.
            if j % 7 == 5 or j % 7 == 6:

                # Computes the morning bedrooms consumption.
                l1 = mins*j+sub.rd_var.norm(param["Bedrooms Morning Time (WE) [h]"][0]*60,
                                            param["Bedrooms Morning Time (WE) [h]"][1]*60,
                                            True)
                l2 = l1+sub.rd_var.norm(param["Bedrooms Morning Duration [min]"][0],
                                        param["Bedrooms Morning Duration [min]"][1],
                                        True)
                power = sub.rd_var.norm(param["Bedrooms Power [W]"][0], param["Bedrooms Power [W]"][1], False)
                active_power[l1:l2] += power

                # Computes the evening bedrooms consumption.
                l1 = mins*j+sub.rd_var.norm(param["Bedrooms Evening Time (WE) [h]"][0]*60,
                                            param["Bedrooms Evening Time (WE) [h]"][1]*60,
                                            True)
                l2 = l1+sub.rd_var.norm(param["Bedrooms Evening Duration [min]"][0],
                                        param["Bedrooms Evening Duration [min]"][1],
                                        True)
                power = sub.rd_var.norm(param["Bedrooms Power [W]"][0], param["Bedrooms Power [W]"][1], False)
                active_power[l1:l2] += power

                # Computes the morning bathrooms consumption.
                l1 = mins*j+sub.rd_var.norm(param["Bathrooms Morning Time (WE) [h]"][0]*60,
                                            param["Bathrooms Morning Time (WE) [h]"][1]*60,
                                            True)
                l2 = l1+sub.rd_var.norm(param["Bathrooms Morning Duration [min]"][0],
                                        param["Bathrooms Morning Duration [min]"][1],
                                        True)
                power = sub.rd_var.norm(param["Bathrooms Power [W]"][0], param["Bathrooms Power [W]"][1], False)
                active_power[l1:l2] += power

                # Computes the evening bathrooms consumption.
                l1 = mins*j+sub.rd_var.norm(param["Bathrooms Evening Time (WE) [h]"][0]*60,
                                            param["Bathrooms Evening Time (WE) [h]"][1]*60,
                                            True)
                l2 = l1+sub.rd_var.norm(param["Bathrooms Evening Duration [min]"][0],
                                        param["Bathrooms Evening Duration [min]"][1],
                                        True)
                power = sub.rd_var.norm(param["Bathrooms Power [W]"][0], param["Bathrooms Power [W]"][1], False)
                active_power[l1:l2] += power

                # Computes the morning kitchen consumption.
                l1 = mins*j+sub.rd_var.norm(param["Kitchen Morning Time (WE) [h]"][0]*60,
                                            param["Kitchen Morning Time (WE) [h]"][1]*60,
                                            True)
                l2 = l1+sub.rd_var.norm(param["Kitchen Morning Duration [min]"][0],
                                        param["Kitchen Morning Duration [min]"][1],
                                        True)
                power = sub.rd_var.norm(param["Kitchen Power [W]"][0], param["Kitchen Power [W]"][1], False)
                active_power[l1:l2] += power

                # Computes the evening kitchen consumption.
                l1 = mins*j+sub.rd_var.norm(param["Kitchen Evening Time (WE) [h]"][0]*60,
                                            param["Kitchen Evening Time (WE) [h]"][1]*60,
                                            True)
                l2 = l1+sub.rd_var.norm(param["Kitchen Evening Duration [min]"][0],
                                        param["Kitchen Evening Duration [min]"][1],
                                        True)
                power = sub.rd_var.norm(param["Kitchen Power [W]"][0], param["Kitchen Power [W]"][1], False)
                active_power[l1:l2] += power

            # Computes the evening lounge consumption.
            l1 = mins*j+sub.rd_var.norm(param["Lounge Evening Time [h]"][0]*60,
                                        param["Lounge Evening Time [h]"][1]*60,
                                        True)
            l2 = l1+sub.rd_var.norm(param["Lounge Evening Duration [min]"][0],
                                    param["Lounge Evening Duration [min]"][1],
                                    True)
            power = sub.rd_var.norm(param["Lounge Power [W]"][0], param["Lounge Power [W]"][1], False)
            active_power[l1:l2] += power
                
            # No light between 8 am and 6 pm in the summer.
            if 90 <= j <= 272:
                active_power[mins*j+480:mins*j+1080] = 0
                                                          
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
