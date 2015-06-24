import random as rd
import numpy as np
import sub.gui
import sub.rd_var
import time


# Defines the boiler function.
def boiler(param, res_dir, text_view):
    
    # Defines the number of minutes in a day
    mins = 1440
    
    # Defines the name of the appliance.
    name = "Boiler"
        
    # Starts a timer.
    start_global_time = time.time()
    
    # Writes intro to terminal.
    sub.gui.display(text_view, "New "+name+" Consumption Simulation!", "red")
    
    # Repeats the following for each house.
    for i in range(int(round(param["Number of Houses"][0]))):
        
        # Starts a timer.
        start_local_time = time.time()
        
        # Initializes the active power vector.
        volume = np.zeros(mins*param["Number of Days"][0])
            
        # Repeats the following for each day.
        for j in range(int(round(param["Number of Days"][0]))):
            
            # Repeats the following for each person.
            for k in range(int(round(param["Number of People"][0]))):
                
                # Continues only if the day is a week day.
                if j % 7 != 5 and j % 7 != 6:
                    
                    # Computes a morning bath if prob is OK.
                    if 100*rd.random() <= param["Bath Morning Prob [%]"][0]:
                        l1 = mins*j+sub.rd_var.norm(param["Morning Time [hour]"][0]*60,
                                                    param["Morning Time [hour]"][1]*60,
                                                    True)
                        l2 = l1+sub.rd_var.norm(param["Bath Duration [min]"][0],
                                                param["Bath Duration [min]"][1],
                                                True)
                        vol = sub.rd_var.norm(param["Bath Flow [l/min]"][0], param["Bath Flow [l/min]"][1], False)/3
                        volume[l1:l2] += vol
                        
                    # Computes an afternoon bath if prob is OK.
                    if 100*rd.random() <= param["Bath Afternoon Prob [%]"][0]:
                        l1 = mins*j+sub.rd_var.norm(param["Afternoon Time [hour]"][0]*60,
                                                    param["Afternoon Time [hour]"][1]*60,
                                                    True)
                        l2 = l1+sub.rd_var.norm(param["Bath Duration [min]"][0],
                                                param["Bath Duration [min]"][1],
                                                True)
                        vol = sub.rd_var.norm(param["Bath Flow [l/min]"][0], param["Bath Flow [l/min]"][1], False)/3
                        volume[l1:l2] += vol
                        
                    # Computes an evening bath if prob is OK.
                    if 100*rd.random() <= param["Bath Evening Prob [%]"][0]:
                        l1 = mins*j+sub.rd_var.norm(param["Evening Time [hour]"][0]*60,
                                                    param["Evening Time [hour]"][1]*60,
                                                    True)
                        l2 = l1+sub.rd_var.norm(param["Bath Duration [min]"][0],
                                                param["Bath Duration [min]"][1],
                                                True)
                        vol = sub.rd_var.norm(param["Bath Flow [l/min]"][0], param["Bath Flow [l/min]"][1], False)/3
                        volume[l1:l2] += vol
                        
                    # Computes a morning shower if prob is OK.
                    if 100*rd.random() <= param["Shower Morning Prob [%]"][0]:
                        l1 = mins*j+sub.rd_var.norm(param["Morning Time [hour]"][0]*60,
                                                    param["Morning Time [hour]"][1]*60,
                                                    True)
                        l2 = l1+sub.rd_var.norm(param["Shower Duration [min]"][0],
                                                param["Shower Duration [min]"][1],
                                                True)
                        vol = sub.rd_var.norm(param["Shower Flow [l/min]"][0], param["Shower Flow [l/min]"][1], False)/3
                        volume[l1:l2] += vol
                        
                    # Computes an afternoon shower if prob is OK.
                    if 100*rd.random() <= param["Shower Afternoon Prob [%]"][0]:
                        l1 = mins*j+sub.rd_var.norm(param["Afternoon Time [hour]"][0]*60,
                                                    param["Afternoon Time [hour]"][1]*60,
                                                    True)
                        l2 = l1+sub.rd_var.norm(param["Shower Duration [min]"][0],
                                                param["Shower Duration [min]"][1],
                                                True)
                        vol = sub.rd_var.norm(param["Shower Flow [l/min]"][0], param["Shower Flow [l/min]"][1], False)/3
                        volume[l1:l2] += vol
                        
                    # Computes an evening shower if prob is OK.
                    if 100*rd.random() <= param["Shower Evening Prob [%]"][0]:
                        l1 = mins*j+sub.rd_var.norm(param["Evening Time [hour]"][0]*60,
                                                    param["Evening Time [hour]"][1]*60,
                                                    True)
                        l2 = l1+sub.rd_var.norm(param["Shower Duration [min]"][0],
                                                param["Shower Duration [min]"][1],
                                                True)
                        vol = sub.rd_var.norm(param["Shower Flow [l/min]"][0], param["Shower Flow [l/min]"][1], False)/3
                        volume[l1:l2] += vol
                        
                # Continues only if the day is a weekend day.
                if j % 7 == 5 or j % 7 == 6:

                    # Computes a morning bath if prob is OK.
                    if 100*rd.random() <= param["Bath Morning Prob (WE) [%]"][0]:
                        l1 = mins*j+sub.rd_var.norm(param["Morning Time (WE) [hour]"][0]*60,
                                                    param["Morning Time (WE) [hour]"][1]*60,
                                                    True)
                        l2 = l1+sub.rd_var.norm(param["Bath Duration [min]"][0],
                                                param["Bath Duration [min]"][1],
                                                True)
                        vol = sub.rd_var.norm(param["Bath Flow [l/min]"][0], param["Bath Flow [l/min]"][1], False)/3
                        volume[l1:l2] += vol

                    # Computes an afternoon bath if prob is OK.
                    if 100*rd.random() <= param["Bath Afternoon Prob (WE) [%]"][0]:
                        l1 = mins*j+sub.rd_var.norm(param["Afternoon Time (WE) [hour]"][0]*60,
                                                    param["Afternoon Time (WE) [hour]"][1]*60,
                                                    True)
                        l2 = l1+sub.rd_var.norm(param["Bath Duration [min]"][0],
                                                param["Bath Duration [min]"][1],
                                                True)
                        vol = sub.rd_var.norm(param["Bath Flow [l/min]"][0], param["Bath Flow [l/min]"][1], False)/3
                        volume[l1:l2] += vol

                    # Computes an evening bath if prob is OK.
                    if 100*rd.random() <= param["Bath Evening Prob (WE) [%]"][0]:
                        l1 = mins*j+sub.rd_var.norm(param["Evening Time (WE) [hour]"][0]*60,
                                                    param["Evening Time (WE) [hour]"][1]*60,
                                                    True)
                        l2 = l1+sub.rd_var.norm(param["Bath Duration [min]"][0],
                                                param["Bath Duration [min]"][1],
                                                True)
                        vol = sub.rd_var.norm(param["Bath Flow [l/min]"][0], param["Bath Flow [l/min]"][1], False)/3
                        volume[l1:l2] += vol

                    # Computes a morning shower if prob is OK.
                    if 100*rd.random() <= param["Shower Morning Prob (WE) [%]"][0]:
                        l1 = mins*j+sub.rd_var.norm(param["Morning Time (WE) [hour]"][0]*60,
                                                    param["Morning Time (WE) [hour]"][1]*60,
                                                    True)
                        l2 = l1+sub.rd_var.norm(param["Shower Duration [min]"][0],
                                                param["Shower Duration [min]"][1],
                                                True)
                        vol = sub.rd_var.norm(param["Shower Flow [l/min]"][0], param["Shower Flow [l/min]"][1], False)/3
                        volume[l1:l2] += vol

                    # Computes an afternoon shower if prob is OK.
                    if 100*rd.random() <= param["Shower Afternoon Prob (WE) [%]"][0]:
                        l1 = mins*j+sub.rd_var.norm(param["Afternoon Time (WE) [hour]"][0]*60,
                                                    param["Afternoon Time (WE) [hour]"][1]*60,
                                                    True)
                        l2 = l1+sub.rd_var.norm(param["Shower Duration [min]"][0],
                                                param["Shower Duration [min]"][1],
                                                True)
                        vol = sub.rd_var.norm(param["Shower Flow [l/min]"][0], param["Shower Flow [l/min]"][1], False)/3
                        volume[l1:l2] += vol

                    # Computes an evening shower if prob is OK.
                    if 100*rd.random() <= param["Shower Evening Prob (WE) [%]"][0]:
                        l1 = mins*j+sub.rd_var.norm(param["Evening Time (WE) [hour]"][0]*60,
                                                    param["Evening Time (WE) [hour]"][1]*60,
                                                    True)
                        l2 = l1+sub.rd_var.norm(param["Shower Duration [min]"][0],
                                                param["Shower Duration [min]"][1],
                                                True)
                        vol = sub.rd_var.norm(param["Shower Flow [l/min]"][0], param["Shower Flow [l/min]"][1], False)/3
                        volume[l1:l2] += vol

                # Computes the number of times the sink is used.
                sink = sub.rd_var.norm(param["Sink Cycles"][0], param["Sink Cycles"][1], True)

                # Repeats the following for each sink utilisation.
                for l in range(sink):
                    
                    # Computes the sink start, end and consumption.
                    l1 = mins*j+sub.rd_var.uni(0, mins, True)
                    l2 = l1+sub.rd_var.norm(param["Sink Duration [min]"][0], param["Sink Duration [min]"][1], True)
                    vol = sub.rd_var.norm(param["Sink Flow [l/min]"][0], param["Sink Flow [l/min]"][1], False)/3
                    volume[l1:l2] += vol

        # Prapares the data to be saved in a .csv file.
        csv_data = map(list, zip(*[volume]))

        # Defines and opens the .csv file.
        csv_file = res_dir+"/"+"house_%000006d.csv" % (i+1)
        fid_w = open(csv_file, "w")

        # Saves the data to the .csv file.
        np.savetxt(fid_w, csv_data, fmt="%.5e", delimiter=",")

        # Computes the daily average volume.
        avg_volume = sum(volume)/param["Number of Days"][0]

        # Computes the local simulation time.
        local_time = time.time()-start_local_time

        # Writes the house status to the terminal.
        text = "House %d:" % (i+1)
        sub.gui.display(text_view, text, "blue")
        text = "Daily average volume = %.3f litres." % avg_volume
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
