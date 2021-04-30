# -*- coding: utf-8 -*-

import pandas as pd
import tkinter
from random import randrange
import numpy as np
import math
  
class AnnotateData():
    def __init__(self):
        self.quote_data = pd.read_csv('quote_data.csv')
        self.iteration = 0
        #print(self.quote_data.get_value(self.iteration, 'Scare_Quote:'))
        #print(self.quote_data['Scare_Quote:'])
        self.paragraph_text = self.quote_data.get_value(self.iteration, 'Paragraph:')
        self.quote_text = self.quote_data.get_value(self.iteration, 'Quote:')
        
        self.top = tkinter.Tk()
        self.paragraph = tkinter.Label(self.top, text="Paragraph:\n" + self.paragraph_text, wraplength=1000)
        self.quote = tkinter.Label(self.top, text="Quote:\n" + self.quote_text, wraplength=1000)

        self.yes_button = tkinter.Button(self.top, text ="Scare Quote", command = self.yesClick)
        self.no_button = tkinter.Button(self.top, text="Not A Scare Quote", command = self.noClick)
        self.idk_button = tkinter.Button(self.top, text="Don't know", command = self.idkClick)


        self.paragraph.pack(side=tkinter.TOP, padx=5, pady=5)
        self.quote.pack(side=tkinter.TOP, padx=5, pady=5)
        self.yes_button.pack(side=tkinter.LEFT, padx=5, pady=5)
        self.no_button.pack(side=tkinter.LEFT, padx=5, pady=5)
        self.idk_button.pack(side=tkinter.LEFT, padx=5, pady=5)
        
        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.top.mainloop()
        
        
    def on_closing(self):
        if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.quote_data.to_csv('quote_data.csv', index=False)
            self.top.destroy()
            
        
    def get_iteration(self):
        return self.iteration
    
    
    def set_iteration(self, number):
        self.iteration = number
        return
    
        
    def generate_new_iteration(self):
        # Check if there exists an unannotated entry
        sq_values = self.quote_data['Scare_Quote:']
        check_entries = True if True in np.isnan(np.array(sq_values)) else False
        if check_entries:
            number = randrange(len(self.quote_data))
            data = self.quote_data.get_value(number, 'Scare_Quote:')
            if np.isnan(data):
                return number
            else: 
                return self.generate_new_iteration()
        else:
            return 0
        
        
    def update(self):
        new_iteration = self.generate_new_iteration()
        print('New iteration is: ' + str(new_iteration))
        self.set_iteration(new_iteration)
        
        paragraph_text = self.quote_data.get_value(new_iteration, 'Paragraph:')
        self.paragraph.configure(text="Paragraph:\n" + paragraph_text)
        
        quote_text = self.quote_data.get_value(new_iteration, 'Quote:')
        self.quote.configure(text="Quote:\n" + quote_text)
        
        
    def yesClick(self):
        iteration = self.get_iteration()
        self.quote_data['Scare_Quote:'][iteration] = 1
        
        self.update()
        
        print("Yes Clicked")
        
   
    def noClick(self):
        iteration = self.get_iteration()
        self.quote_data['Scare_Quote:'][iteration] = 0
        
        self.update()
        
        print("No Clicked")
        
    
    def idkClick(self):
        iteration = self.get_iteration()
        self.quote_data['Scare_Quote:'][iteration] = 2
        
        self.update()
        
        print("Idk Clicked")
        
app=AnnotateData()
