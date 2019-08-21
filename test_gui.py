# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 09:54:37 2019

@author: Steffen 000
"""

from Tkinter import *
import Tkinter as ttk
from ttk import *
from PIL import Image, ImageTk


from feats import feat_list, feat_N, feat_description
from backgrounds import bg_list, bg_N, bg_description
from races import race_list, race_N, race_description, race_dict,subrace_dict
from classes import class_list, class_N, class_description, class_dict



root = Tk()
root.title("Create character")
root.state('zoomed')

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 25, padx = 25)


# Create a Tkinter variable
tkvar1 = StringVar()
tkvar2 = StringVar()
tkvar3 = StringVar()
tkvar4 = StringVar()

v1 = StringVar(mainframe,'0')#variable for race
v11 = StringVar(mainframe,'0')#variable for subrace
v2 = StringVar(mainframe,'0')#variable for class

#----- Races and subraces in GUI
raceLabel = Label(mainframe, text='Choose a race')
raceLabel.grid(row = 1, column = 0)
raceText = Text(mainframe, height=25, width=100)
raceText.grid(row = 3, column =2,rowspan=18,columnspan=5)

subraceLabel = Label(mainframe,text='Choose a subrace')
subraceLabel.grid(row=1,column = 8)
subraceText = Text(mainframe, height=25, width=60)
subraceText.grid(row = 3, column =9,rowspan=18,columnspan=5)

for (text,value) in race_dict.items():
    rad1 = Radiobutton(mainframe, text=text, variable=v1, value=value)#.pack(side=TOP,ipady=5)
    if int(value)%2==0:   
        rad1.grid(row = 3+int(value)/2, column = 0, sticky=W)
    else:
        rad1.grid(row = 3+int(value)/2, column = 1, sticky=W)
rad11 = Radiobutton(mainframe,text='None                                                                      ',variable =v11, value ='0')
rad11.grid(row=3,column =8,sticky=W)
       
#------ Classes and subclasses in GUI
classLabel = Label(mainframe, text="Choose a class")
classLabel.grid(row = 50, column = 0)
classText = Text(mainframe, height=25, width=100)
classText.grid(row = 51, column =2,rowspan=20)

for (text,value) in class_dict.items():
    rad2 = Radiobutton(mainframe, text=text, variable=v2, value=value)#.pack(side=TOP,ipady=5)
    if int(value)%2==0:
        rad2.grid(row = 51+int(value)/2, column = 0, sticky=W)
    else:
        rad2.grid(row = 51+int(value)/2, column = 1, sticky=W)
        
       


#bgLabel = Label(mainframe, text="Choose a background")
#bgLabel.grid(row = 5, column = 2)
#bgMenu = OptionMenu(mainframe, tkvar3, bg_list[0], *bg_list)
#bgMenu.grid(row = 2, column = 2)
#bgText = Text(mainframe, height=20, width=50)
#bgText.grid(row = 50, column = 2,rowspan=20)
#
#
#featsLabel = Label(mainframe, text="Choose a feat")
#featsLabel.grid(row = 1, column = 2)
#featsMenu = OptionMenu(mainframe, tkvar4, feat_list[0], *feat_list)
#featsMenu.grid(row = 2, column = 2)
#featsText = Text(mainframe, height=20, width=50)
#featsText.grid(row = 50, column = 2,rowspan=20)

# update gui when pressing button
def change_radio1(*args):
    var1 = int(v1.get())
    raceText.delete(1.0, END)
    quote = race_description(race_list[var1])[0]
    raceText.insert(END,quote)
    subraces = subrace_dict(race_list[var1])
    for i in xrange(10):#programming gore to remove subclass buttons if they shouldn't be there... raise range if its not high enough
        clearLabel = Label(mainframe,text='''                                                                         ''')
        clearLabel.grid(row=3+i,column=8,sticky=W)        
    for (text,value) in subraces.items():
        rad11 = Radiobutton(mainframe, text=text, variable=v11, value=value)
        rad11.grid(row = 3+int(value), column = 8, sticky=W)
    load = Image.open('pictures/'+race_list[var1]+'.png')
    image2 = load.resize((220,260),Image.ANTIALIAS)
    render = ImageTk.PhotoImage(image2)
    img = Label(mainframe,image=render)
    img.image = render
    #img.resize((250,250),Image.ANTIALIAS)
    img.grid(row=13,column=8,rowspan=5)
    
    
def change_radio11(*args):
    var1 = int(v1.get())
    var11 = int(v11.get())
    subraceText.delete(1.0,END)
    quote = race_description(race_list[var1])[1][var11]
    subraceText.insert(END,quote)  

def change_radio2(*args):
    var2 = v2.get()
    for i in xrange(class_N):
        if class_list[int(var2)] == class_list[i]:
            classText.delete(1.0, END)
            quote = class_description(class_list[i])
            classText.insert(END,quote)
            break
        else:
            classText.delete(1.0, END)
            quote = 'Not in list'        
            classText.insert(END,quote)    
    
#def change_dropdown3(*args):
#    var3 = tkvar3.get()
#    for i in xrange(bg_N):
#        if var3==bg_list[i]:
#            bgText.delete(1.0, END)
#            quote = bg_description(bg_list[i])
#            bgText.insert(END,quote)
#            break
#
#        else:
#            bgText.delete(1.0, END)
#            quote = 'Not in list'
#            bgText.insert(END,quote)
#            
#def change_dropdown4(*args):
#    var4 = tkvar4.get()
#    for i in xrange(feat_N):
#        if var4==feat_list[i]:
#            featsText.delete(1.0, END)
#            quote = feat_description(feat_list[i])
#            featsText.insert(END,quote)
#            break
#
#        else:
#            featsText.delete(1.0, END)
#            quote = 'Not in list'
#            featsText.insert(END,quote) 

# link function to change dropdown
v1.trace('w',change_radio1)
v11.trace('w',change_radio11)
v2.trace('w',change_radio2)
#tkvar3.trace('w',change_dropdown3)
#tkvar4.trace('w',change_dropdown4)



      



root.mainloop()
















