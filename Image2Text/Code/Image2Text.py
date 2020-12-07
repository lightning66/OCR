#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required modules from tkinter.
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import numpy as np

#download and install pillow:
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
from PIL import Image, ImageTk

#Download and install tesseract from the link below:
#https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.1.0-bibtag19.exe
#To read texts from an image
import pytesseract
#refer to the tesseract directory, where the "exe" file is stored
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization.
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

        
        
    #Creation of init_window
    def init_window(self):

        #Changing the title of our master widget      
        self.master.title("Image2Text")
        
        self.pack(fill=BOTH, expand=1)
        
        #Creating a label within the widget
        self.labelFrame = ttk.LabelFrame(self, text = 
                                         "Open a file")
        self.labelFrame.grid(column = 0, row = 0,
                            padx = 20, pady = 20)
        self.button()
    
    
    #Define button label in "text" and what it does in "command"
    def button(self):
        self.button = ttk.Button(self.labelFrame,
                                text = 'Browse a file',
                                command = self.showImg)
        self.button.grid(column = 0, row = 0)
    
    

    #This function is used in button function
    def showImg(self):
        self.filename = filedialog.askopenfilename(
        initialdir = "/", title = 'Select a file',
        filetype = (('png', '*.png'),
                    ('jpg', '*.jpg'),
                    ('jpeg', '*.jpeg'),
                    ('bmp', '*.bmp'),
                   ('All files', '*.*')))
        
        load_img = Image.open(self.filename)
        
        #For processing the image in tesseract it should be converted to numpy array
        img_arr = np.array(load_img)
        
        #Read the text from an image using tesseract
        text = pytesseract.image_to_string(img_arr)
        
        #Save the text in a "txt" file with the filename same as the original image
        if self.filename[-4:] == 'jpeg':
            text_file = open(self.filename[:-4] + 'txt', 'w')
            n = text_file.write(text)
            text_file.close()
            
            #To print final message to users.
            messagebox.showinfo('Editable text file is successfully saved in:', self.filename[:-4] + 'txt')
            
            
        else:
            text_file = open(self.filename[:-3] + 'txt', 'w')
            n = text_file.write(text)
            text_file.close()
            
            #To print final message to users.
            messagebox.showinfo('Editable text file is successfully saved in:', self.filename[:-3] + 'txt')        
        
        
        #For displaying the image in tkinter
        render = ImageTk.PhotoImage(load_img)

        # labels can be text or images
        img = Label(self, image=render)
        
        img.image = render
        img.place(x=0, y=0)




# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()  


# In[ ]:




