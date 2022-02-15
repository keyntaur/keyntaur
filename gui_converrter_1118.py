# Learn how to create Graphic User Interface(GUI)
# convert kilometers into miles
# Use tkinter module
# in Chpt 13, section 1
# steps:

import tkinter # it is a GUI module
from tkinter import messagebox # import messagebox class

class KiloConvertGUI:

    def __init__(self):
        # add the main window

        self.main_window=tkinter.Tk() # assign a window as the interface's main window

        # add title to the window
        self.main_window.wm_title("ISA281-kirpacas")

        # add three frames on the window
        self.top_frame=tkinter.Frame() # add a frame as top_frame on the main window
        self.mid_frame=tkinter.Frame() # add a frame as mid_frame on the main window
        self.bottom_frame=tkinter.Frame() # add a frame as bottom_frame on the main window


        # add two objects on the top frame
        self.prompt_label=tkinter.Label(self.top_frame, text="Enter a distance in kilometers: ")
        self.kilo_entry=tkinter.Entry(self.top_frame, width=10)

        # pack objects in top frame
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # add objects to mid frame
        self.desc_label=tkinter.Label(self.mid_frame, text='Converted to miles:')

        # create a middle man
        self.value=tkinter.StringVar() # create an object to hold the converted value

        # add a blank label to display the mileage
        self.mile_label=tkinter.Label(self.mid_frame, textvariable=self.value)

        # pack objects in top frame
        self.desc_label.pack(side='left')
        self.mile_label.pack(side='left')

        # add two objects to the bottom frame
        self.calc_button=tkinter.Button(self.bottom_frame, text='Convert', \
                                        command=self.convert)

        # If the button is clicked, then convert method is triggered
        self.quit_button=tkinter.Button(self.bottom_frame, text='Quit', \
                                        command=self.main_window.destroy)
        # If the 'QUIT' button is clicked, then destroy method will close the window

        # pack the above two buttons in bottom frame
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='right')

        # pack three frames in the window
        self.top_frame.pack()

        # pack three frames in the window
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # make sure the main window is running
        tkinter.mainloop()

    def convert(self):
        kilo=float(self.kilo_entry.get()) #get input for km as a float num
        miles=kilo*0.6214 # do the calculations

        self.value.set(format(miles, ',.2f')) # put the miles in self.value object

        tkinter.messagebox.showinfo('Result', str(kilo) + ' kilometers are equal to ' + \
                                    format(miles, ',.2f') + ' miles.')



def main():

    kilo_conv=KiloConvertGUI()

main()
        
        



        
