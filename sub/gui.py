import collections
import shutil
import pango
import glob
import time
import gtk
import sys
import os
import app


# Defines the Simulator class.
class Simulator:

    # Defines the __init__ function.
    def __init__(self):
        
        # Defines the main directory path.
        root_path = os.path.dirname(os.path.realpath(__file__))
        
        # Defines the default configuration directory path.
        default_path = root_path.replace("sub", "default_config")
        root_path = root_path.replace("sub", "")
        
        # Defines the simulation directories.
        self.sim_path = ""
        self.conf_path = ""
        self.res_path = ""
        
        # List .csv files in default configuration directory.
        default_csv = glob.glob(os.path.join(default_path, "*.csv"))
        
        # Repeats the following for each configuration file.
        for csv in default_csv:
            
            # Gets the appliance name from the file name.
            csv_path_list = csv.split(os.sep)
            appliance = csv_path_list[-1][:-4]
            
            # Defines the ordered dictionary.
            exec "%s = collections.OrderedDict()" % appliance

            # Opens the configuration file for the appliance.
            fid = open(csv, "r")
            
            # Gets next line, removes ending \n and defines the key values.
            line = next(fid)
            line = line.strip()
            key = line.split(",")

            # Gets next line, removes ending \n and defines the mu values.
            line = next(fid)
            line = line.strip()
            mu = line.split(",")
            
            # Gets next line, removes ending \n and defines the sigma values.
            line = next(fid)
            line = line.strip()
            sigma = line.split(",")
            
            # Repeats the following for each key.
            for j in range(len(key)):
                
                # Builds the ordered dictionary.
                if key[j] == "Name of the Simulation" or key[j] == "Keeps Water Warm?" or key[j] == "Induction?":
                    exec """%s["%s"] = [mu[%d], sigma[%d]]""" % (appliance, key[j], j, j)
                elif key[j] == "Number of Houses" or key[j] == "Number of Days" or key[j] == "Number of People":
                    exec """%s["%s"] = [int(mu[%d]), sigma[%d]]""" % (appliance, key[j], j, j)
                elif sigma[j] == "-":
                    exec """%s["%s"] = [float(mu[%d]), sigma[%d]]""" % (appliance, key[j], j, j)
                else:
                    exec """%s["%s"] = [float(mu[%d]), float(sigma[%d])]""" % (appliance, key[j], j, j)

        # Defines the list of icons for the GUI toolbar.
        icon = ["coffee_machine", "kettle", "microwave", "oven", "stove", "toaster", "freezer", "fridge", "base_load",
                "boiler", "dish_washer", "tumble_dryer", "washing_machine", "hifi", "ict", "tv", "hair_dryer", "iron",
                "lighting", "vacuum_cleaner"]

        # Defines the list of labels for the GUI toolbar.
        label = ["Coffee Machine", "Kettle", "Microwave", "Oven", "Stove", "Toaster", "Freezer", "Fridge", "Base Load",
                 "Boiler", "Dish Washer", "Tumble Dryer", "Washing Machine", "Hifi", "ICT", "TV", "Hair Dryer", "Iron",
                 "Lighting", "Vacuum Cleaner"]
        
        # Creates the main GUI window.
        win = gtk.Window()
        win.set_title("BehavSim - The SEMIAH Consumption Simulation Tool")
        win.set_icon_from_file("icons/simulator.png")
        win.resize(748, 640)
        win.set_position(gtk.WIN_POS_CENTER)
        
        # Creates the GUI vbox.
        vbox = gtk.VBox()
        
        # Creates the GUI toolbars.
        toolbar = gtk.Toolbar()
        toolbar.set_style(gtk.TOOLBAR_ICONS)
        toolbar1 = gtk.Toolbar()
        toolbar1.set_style(gtk.TOOLBAR_ICONS)
        toolbar2 = gtk.Toolbar()
        toolbar2.set_style(gtk.TOOLBAR_ICONS)
        
        # Creates the GUI scrolled window for the terminal.
        scroll_win = gtk.ScrolledWindow()
        scroll_win.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        
        # Creates the text view for the terminal.
        text_view = gtk.TextView()
        text_view.set_editable(False)
        text_view.set_cursor_visible(False)
        text_view.modify_font(pango.FontDescription("monospace"))
        text_view.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse('#000000'))
        
        # Adds the text view to the scrolled window.
        scroll_win.add(text_view)

        # Repeats the following for each icon.
        for i in range(len(icon)):
            
            # Creates an image from the icon for the GUI toolbar button.
            image_l = "image_%02d" % i
            image_r = "gtk.Image()"
            exec "%s = %s" % (image_l, image_r)
            exec """%s.set_from_file("icons/%s.png")""" % (image_l, icon[i])
            
            # Creates the GUI toolbar button.
            button_l = "button_%02d" % i
            button_r = "gtk.ToolButton()"
            exec "%s = %s" % (button_l, button_r)
            exec """%s.set_tooltip_text("%s")""" % (button_l, label[i])
            exec "%s.set_icon_widget(%s)" % (button_l, image_l)
            exec """%s.connect("clicked", self.msg_dlg, "%s", "%s", %s, text_view)""" % (button_l, label[i], icon[i],
                                                                                         icon[i])
            
            # Adds the GUI toolbar button.
            if i < 10:
                exec "toolbar1.add(%s)" % button_l
            else:
                exec "toolbar2.add(%s)" % button_l
                
        # Creates an image from the icon for the menu toolbar buttons.
        config_image = gtk.Image()
        config_image.set_from_file("icons/config.png")
        run_image = gtk.Image()
        run_image.set_from_file("icons/run.png")
        help_image = gtk.Image()
        help_image.set_from_file("icons/help.png")
        quit_image = gtk.Image()
        quit_image.set_from_file("icons/quit.png")
        
        # Creates the menu toolbar buttons.
        config_button = gtk.ToolButton()
        config_button.set_tooltip_text("Start Configuration")
        config_button.set_icon_widget(config_image)
        config_button.connect("clicked",
                              self.create_sim_dir,
                              root_path,
                              text_view)
        run_button = gtk.ToolButton()
        run_button.set_tooltip_text("Run Simulation")
        run_button.set_icon_widget(run_image)
        run_button.connect("clicked",
                           self.run_sim,
                           root_path,
                           text_view)
        help_button = gtk.ToolButton()
        help_button.set_tooltip_text("Help")
        help_button.set_icon_widget(help_image)
        help_button.connect("clicked", self.sim_help)
        quit_button = gtk.ToolButton()
        quit_button.set_tooltip_text("Quit Application")
        quit_button.set_icon_widget(quit_image)
        quit_button.connect("clicked", self.quit_gtk)
        
        # Adds the menu toolbar buttons.
        toolbar.add(config_button)
        toolbar.add(run_button)
        toolbar.add(help_button)
        toolbar.add(quit_button)

        # Adds the toolbars to the GUI vbox.
        vbox.pack_start(toolbar, False, False, 0)
        vbox.pack_start(toolbar1, False, False, 0)
        vbox.pack_start(toolbar2, False, False, 0)
        
        # Adds the scrolled window to the GUI vbox.
        vbox.pack_start(scroll_win, True, True, 0)
        
        # Adds the vbox to the main GUI window.
        win.add(vbox)
        win.connect("destroy", self.quit_gtk)
        win.show_all()
        
    # Defines the sim_help function.
    def sim_help(self, button):
        
        font_desc = pango.FontDescription("monospace")
        help_window = gtk.Window() 
        help_window.set_modal(True)
        help_window.set_title("Help")
        help_window.set_border_width(0)
        help_window.set_icon_from_file("icons/simulator.png")
        help_window.set_position(gtk.WIN_POS_CENTER)
        help_window.resize(800, 600)
        help_scroll_window = gtk.ScrolledWindow()
        help_scroll_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        text = "Welcome to BehavSim, the SEMIAH Consumption Simulation Tool!\n"
        text += "============================================================\n"
        text += "\n"
        text += "To use BehavSim, you need to:\n"
        text += "1. Configure the simulation\n"
        text += "2. Run the simulation\n"
        text += "\n"
        text += "1. Configure the simulation\n"
        text += "---------------------------\n"
        text += "\n"
        text += "- Click the blue cross button (top left)\n"
        text += "  -> Opens a dialog\n"
        text += "- Create a new folder (recommended)\n"
        text += "  -> Confirmation in terminal:\n"
        text += "     >>> New Simulation Started!\n"
        text += "     >>> /media/fep/DATA/HEVs/SEMIAH/Simulator/test\n"
        text += "  !! CAUTION !! If you use an existing folder, all its content will be deleted !!\n"
        text += "  Two folders are created in the simulation folder: configuration and results\n"
        text += "  If you try to add appliances (click the appliances buttons) before selecting a simulation folder:\n"
        text += "  -> Error message in terminal:\n"
        text += "     >>> No simulation directory selected! Please click the Start Configuration button!\n"
        text += "- Click the button of the appliances you want to add to the simulation\n"
        text += "  -> Opens a dialog\n"
        text += "- Enter the simulation parameters of the selected appliance\n"
        text += "  -> Confirmation in terminal:\n"
        text += "     >>> New Fridge Configuration Added (fridge)!\n"
        text += "  The parameters of the added appliance are stored in a .csv file in the configuration folder\n"
        text += "  The parameters of the appliances of the same type are stored in the same .csv file (fridge, freezer, etc)\n"
        text += "  Each appliance takes two lines of the .csv files\n"
        text += "  -> First line for average values\n"
        text += "  -> Second line for standard deviation (- if not applicable)\n"
        text += "  You can also manually edit the .csv files to add appliances\n"
        text += "  !! CAUTION !! Do not change the first line (header) of the .csv files !!\n"
        text += "\n"
        text += "2. Run the simulation\n"
        text += "---------------------\n"
        text += "\n"
        text += "- Click the green arrow\n"
        text += "  -> Opens a dialog\n"
        text += "- Select the simulation folder\n"
        text += "  -> The simulation is running\n"
        text += "  -> Confirmation of each simulation of each applince in terminal:\n"
        text += "     >>> New Fridge Consumption Simulation!\n"
        text += "     >>> House 1:\n"
        text += "     >>> Daily average energy = 0.894 kWh.\n"
        text += "     >>> Duration = 0.640 seconds.\n"
        text += "     >>> House 2:\n"
        text += "     >>> Daily average energy = 0.890 kWh.\n"
        text += "     >>> Duration = 0.658 seconds.\n"
        text += "     >>> The Fridge Consumption Simulation took:\n"
        text += "     >>> 0 hours, 0 minutes, and 1.348 seconds.\n"
        text += "  The results are saved in .csv files in the results folder\n"
        text += "  The results of the appliances of the same type are stored in the same folder (fridge, freezer, etc)\n"
        text += "  The results of each appliance are stored in a different .csv file (house_000001.csv, house_000002.csv, etc)\n"
        text += "\n"
        text += "01.07.2015\n"
        text += "Pierre Ferrez\n"
        text += "pierre.ferrez@hevs.ch"
        help_text = gtk.TextView()
        help_text.set_editable(False)
        help_text_buffer = help_text.get_buffer()
        help_text.modify_font(font_desc)
        help_text.set_wrap_mode(gtk.WRAP_WORD)
        help_scroll_window.add(help_text)
        help_window.add(help_scroll_window)
        help_text_buffer.set_text(text)
        help_window.show_all()
        
    # Defines the quit_gtk function.
    def quit_gtk(self, button):
    
        # Quits GTK.
        gtk.main_quit()
        sys.exit()
    
    # Defines the create_sim_dir function.    
    def create_sim_dir(self, button, root_path, text_view):
        
        # Creates a dialog to select a simulation directory.
        dir_dlg = gtk.FileChooserDialog("Select Simulation Folder",
                                        None,
                                        gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
                                        (gtk.STOCK_CANCEL,
                                         gtk.RESPONSE_CANCEL,
                                         gtk.STOCK_OPEN,
                                         gtk.RESPONSE_OK))
        dir_dlg.set_current_folder(root_path)
        res = dir_dlg.run()
        
        # Continues only if the OK button is pressed.
        if res == gtk.RESPONSE_OK:
            
            # Gets the simulation directory and empty it.
            self.sim_path = dir_dlg.get_filename()
            shutil.rmtree(self.sim_path)
            os.mkdir(self.sim_path)
            
            # Closes the dialog.
            dir_dlg.destroy()
            
            # Makes sure the dialog is closed before continuing.
            while gtk.events_pending():
                gtk.main_iteration()
            
            # Creates the configuration directory.
            self.conf_path = self.sim_path+"/configuration"
            os.mkdir(self.conf_path)
            
            # Createst the results directory.
            self.res_path = self.sim_path+"/results"
            os.mkdir(self.res_path)
                
            # Creates a terminal message for the new simulation.
            display(text_view, "New Simulation Started!", "red")
            display(text_view, self.sim_path, "white")
        
        # Closes the dialog.
        dir_dlg.destroy()

    # Defines the msg_dlg function.
    def msg_dlg(self, button, label, folder, param, text_view):
        
        # Continues only if the simulation directory has been selected.
        if self.sim_path == "":
            
            # Creates a terminal error message.
            text = "No simulation directory selected! "
            text += "Please click the Start Configuration button!"
            display(text_view, text, "red")

        else:
            
            # Creates the GUI dialog for the simulation's parameters.
            dialog = gtk.MessageDialog(None,
                                       gtk.DIALOG_MODAL,
                                       gtk.MESSAGE_QUESTION,
                                       gtk.BUTTONS_OK_CANCEL,
                                       None)
            dialog.set_title("New "+label+" Consumption Simulation")
            dialog.set_markup("Please enter the following info:")
            dialog_image = gtk.Image()
            dialog_image.set_from_file("icons/"+folder+".png")
            dialog.set_image(dialog_image)
            
            # Initializes counter i.
            i = 0
        
            # Repeats the following for each simulation field.
            for key, value in param.iteritems():
                
                # Creates GUI elements for input with no sigma.
                if value[1] == "-":
                    
                    # Creates a HBox for the simulation field.
                    hbox_l = "hbox_%02d" % i
                    hbox_r = "gtk.HBox()"
                    exec "%s = %s" % (hbox_l, hbox_r)
                    
                    # Creates the label for the simulation field.
                    label_l = "label1_%02d" % i
                    label_r = """gtk.Label("%s")""" % key
                    exec "%s = %s" % (label_l, label_r)
                    exec "%s.set_size_request(240, 24)" % label_l
                    
                    # Creates the entry for the simulation field.
                    entry_l = "entry1_%02d" % i
                    entry_r = "gtk.Entry()"
                    exec "%s = %s" % (entry_l, entry_r)
                    exec "%s.set_size_request(300,24)" % entry_l
                    exec """%s.set_text("%s")""" % (entry_l, value[0])
    
                    # Adds the label and the entrie to the HBox.
                    exec "%s.add(%s)" % (hbox_l, label_l)
                    exec "%s.add(%s)" % (hbox_l, entry_l)
                    
                    # Adds the HBox to the GUI dialog.
                    exec "dialog.vbox.pack_start(%s, True, True, 0)" % hbox_l
                
                # Creates GUI elements for input with sigma.
                else:
                
                    # Creates a HBox for the appliance field.
                    hbox_l = "hbox_%02d" % i
                    hbox_r = "gtk.HBox()"
                    exec "%s = %s" % (hbox_l, hbox_r)
                    
                    # Creates the label for the average value field.
                    label_l = "label1_%02d" % i
                    label_r = """gtk.Label("%s")""" % key
                    exec "%s = %s" % (label_l, label_r)
                    exec "%s.set_size_request(240, 24)" % label_l
                    
                    # Creates the entry for the average value field.
                    entry_l = "entry1_%02d" % i
                    entry_r = "gtk.Entry()"
                    exec "%s = %s" % (entry_l, entry_r)
                    exec "%s.set_size_request(138, 24)" % entry_l
                    exec """%s.set_text("%s")""" % (entry_l, value[0])
                    
                    # Adds the label and the entrie to the HBox.
                    exec "%s.add(%s)" % (hbox_l, label_l)
                    exec "%s.add(%s)" % (hbox_l, entry_l)
                    
                    # Creates the label for the standard deviation value field.
                    label_l = "label2_%02d" % i
                    label_r = """gtk.Label("+-")"""
                    exec "%s = %s" % (label_l, label_r)
                    exec "%s.set_size_request(24, 24)" % label_l
                    
                    # Creates the entry for the standard deviation value field.
                    entry_l = "entry2_%02d" % i
                    entry_r = "gtk.Entry()"
                    exec "%s = %s" % (entry_l, entry_r)
                    exec "%s.set_size_request(138, 24)" % entry_l
                    exec """%s.set_text("%s")""" % (entry_l, value[1])
                    
                    # Adds the label and the entrie to the HBox.
                    exec "%s.add(%s)" % (hbox_l, label_l)
                    exec "%s.add(%s)" % (hbox_l, entry_l)
                    
                    # Adds the HBox to the GUI dialog.
                    exec "dialog.vbox.pack_start(%s, True, True, 0)" % hbox_l
                    
                # Incrementes counter.
                i += 1
        
            # Reduces spacing and shows all entries of the GUI dialog.
            dialog.vbox.set_spacing(4)
            dialog.show_all()
            
            # Gets dialog resonse.
            res = dialog.run()
            
            # Continues only if "OK" button is pressed.
            if res == gtk.RESPONSE_OK:
                
                new_param = collections.OrderedDict()
                
                # Initializes counter i.
                i = 0
                
                # Repeats the following for each simulation field.
                for key, value in param.iteritems():
                    
                    # Gets values from GUI for input with no sigma.
                    if value[1] == "-":
                        
                        # Gets values from GUI dialog.
                        if key == "Name of the Simulation" or key == "Keeps Water Warm?" or key == "Induction?":
                            exec "val = entry1_%02d.get_text()" % i
                        elif key == "Number of Houses" or key == "Number of Days" or key == "Number of People":
                            exec "val = int(entry1_%02d.get_text())" % i
                        else:
                            exec "val = float(entry1_%02d.get_text())" % i
                        exec """new_param["%s"] = [val, "-"]""" % key

                    # Gets values from GUI for input with sigma.
                    else:
                        
                        # Gets values from GUI dialog.
                        exec "mu = float(entry1_%02d.get_text())" % i
                        exec "sigma = float(entry2_%02d.get_text())" % i
                        exec """new_param["%s"] = [mu,sigma]""" % key
                        
                    # Incrementes counter.
                    i += 1
                
            # Closes the dialog.
            dialog.destroy()
            
            # Makes sure the dialog is closed before continuing.
            while gtk.events_pending():
                gtk.main_iteration()
                
            # Continues only if "OK" button is pressed.
            if res == gtk.RESPONSE_OK:
                
                # Creates a terminal error message.
                name = new_param["Name of the Simulation"][0]
                text = "New "+label+" Configuration Added ("+name+")!"
                display(text_view, text, "blue")
                
                # Defines header, mu and sigma.
                header = []
                mu = []
                sigma = []
                
                # Builds header, mu and sigma from dictionary.
                for key, value in new_param.iteritems():
                    header.append(key)
                    mu.append(str(value[0]))
                    sigma.append(str(value[1]))
                    
                # Defines the configuration file.
                conf_file = self.conf_path+"/"+folder+".csv"
                
                # Saves new config to configuration file.
                if os.path.isfile(conf_file):
                    fid = open(conf_file, "a")
                else:
                    fid = open(conf_file, "w")
                    for i in range(len(header)):
                        fid.write(header[i])
                        if i != len(header)-1:
                            fid.write(",")
                fid.write("\n")
                for i in range(len(mu)):
                    fid.write(mu[i])
                    if i != len(mu)-1:
                        fid.write(",")
                fid.write("\n")
                for i in range(len(sigma)):
                    fid.write(sigma[i])
                    if i != len(sigma)-1:
                        fid.write(",")
                fid.close()

    # Defines the run_sim function.    
    def run_sim(self, button, root_path, text_view):
        
        # Creates a dialog to select a simulation directory.
        run_dlg = gtk.FileChooserDialog("Select Simulation Folder", None, gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
                                        (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        run_dlg.set_current_folder(root_path)
        res = run_dlg.run()
        
        # Continues only if the OK button is pressed.
        if res == gtk.RESPONSE_OK:
            
            # Gets the simulation directory.
            self.sim_path = run_dlg.get_filename()
            
            # Closes the dialog.
            run_dlg.destroy()
            
            # Makes sure the dialog is closed before continuing.
            while gtk.events_pending():
                gtk.main_iteration()
            
            # Creates the configuration and results directories.
            self.conf_path = self.sim_path+"/configuration"
            self.res_path = self.sim_path+"/results"
            
            # Contiunes only if the simulation directory is valid.
            if os.path.isdir(self.conf_path) and os.path.isdir(self.res_path):
                
                # Empties the results directory.
                shutil.rmtree(self.res_path)
                os.mkdir(self.res_path)
                
                # List .csv files in configuration directory.
                csv_files = glob.glob(self.conf_path+"/*.csv")
                
                # Repeats the following for each configuration file.
                for csv in csv_files:
                    
                    # Gets the appliance name from the file name.
                    csv_path_list = csv.split(os.sep)
                    appliance = csv_path_list[-1][:-4]
                    
                    # Defines the ordered dictionnary.
                    param = collections.OrderedDict()
                    
                    # Computes the number of lines in the file.
                    lines = sum(1 for line in open(csv))
                    n = int((lines-1)/2.0)
                    
                    # Opens the configuration file for the appliance.
                    fid = open(csv, "r")
                    
                    # Gets next line and defines the key values.
                    line = next(fid)
                    line = line.strip()
                    key = line.split(",")
                    
                    # Repeats the following for each set of parameters.
                    for i in range(n):
                        
                        # Gets next line and defines the mu values.
                        line = next(fid)
                        line = line.strip()
                        mu = line.split(",")
                        
                        # Gets next line and defines the sigma values.
                        line = next(fid)
                        line = line.strip()
                        sigma = line.split(",")
                        
                        # Repeats the following for each key.
                        for j in range(len(key)):
                            
                            # Builds the ordered dictionnary.
                            if sigma[j] == "-":
                                if key[j] == "Name of the Simulation":
                                    exec """param["%s"] = [mu[%d], sigma[%d]]""" % (key[j], j, j)
                                elif key[j] == "Keeps Water Warm?":
                                    exec """param["%s"] = [mu[%d], sigma[%d]]""" % (key[j], j, j)
                                elif key[j] == "Induction?":
                                    exec """param["%s"] = [mu[%d], sigma[%d]]""" % (key[j], j, j)
                                elif key[j] == "Number of Houses":
                                    exec """param["%s"] = [int(mu[%d]), sigma[%d]]""" % (key[j], j, j)
                                elif key[j] == "Number of Days":
                                    exec """param["%s"] = [int(mu[%d]), sigma[%d]]""" % (key[j], j, j)
                                elif key[j] == "Number of People":
                                    exec """param["%s"] = [int(mu[%d]), sigma[%d]]""" % (key[j], j, j)
                                else:
                                    exec """param["%s"] = [float(mu[%d]), sigma[%d]]""" % (key[j], j, j)
                            else:
                                exec """param["%s"] = [float(mu[%d]), float(sigma[%d])]""" % (key[j], j, j)
                                  
                        # Creates the appliance results directory.
                        res_dir = self.res_path+"/"
                        res_dir += param["Name of the Simulation"][0]
                        os.mkdir(res_dir)
                        
                        # Runs the simulation.
                        exec "app.%s(param, res_dir, text_view)" % appliance
                
            else:
                
                # Creates a terminal error message.
                text = "Invalid simulation directory! Please select a valid directory!"
                display(text_view, text, "red")
                
        # Closes the dialog.
        run_dlg.destroy()


# Defines the display function.    
def display(text_view, text, color):

    # Defines the text view buffer
    text_buffer = text_view.get_buffer()
    
    # Defines bold and color tags.
    bold_tag = text_buffer.create_tag(None, weight=pango.WEIGHT_BOLD)
    green_tag = text_buffer.create_tag(None, foreground="#33CC33")
    red_tag = text_buffer.create_tag(None, foreground="#FF0000")
    blue_tag = text_buffer.create_tag(None, foreground="#33CCFF")
    white_tag = text_buffer.create_tag(None, foreground="#FFFFFF")
    
    # Select the desired color tag.
    tag = white_tag
    if color == "green":
        tag = green_tag
    if color == "red":
        tag = red_tag
    if color == "blue":
        tag = blue_tag

    # Writes the left part of the command (date and time).
    position = text_buffer.get_end_iter()
    prompt = time.strftime("%Y-%m-%d %H:%M:%S")+" >>> "
    text_buffer.insert_with_tags(position, prompt, green_tag, bold_tag)

    # Writes the simulation intro.
    position = text_buffer.get_end_iter()
    text_buffer.insert_with_tags(position, text+"\n", tag, bold_tag)
    
    # Scrolls to the end of the text.
    while gtk.events_pending():
        gtk.main_iteration()
    position = text_buffer.get_end_iter()
    text_view.scroll_to_iter(position, 0)
    while gtk.events_pending():
        gtk.main_iteration()
