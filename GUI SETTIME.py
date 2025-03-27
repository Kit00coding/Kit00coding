#Mya Davis
#This program creates a GUI interface for the clock.py class
#It allows the user to change and set the time and date using scroll bars and buttons

#Import tkinter to make the scroll bars and buttons/ import clock.py to use the time and date changing methods
import tkinter as tk
from Clock import Clock

#Create and name the screen the GUI interface will appear in
screen = tk.Tk()
screen.title("Clock")
#Make a size for the screen to fit the GUI interface
screen.geometry("700x700")
clockobject=Clock()


    
#Create a method where all the methods from Clock.py are called to change the string at the top of the GUI  
def SetClock(self):

    month= self.Monthbox.curselection()[0]+1
    day= self.Daybox.curselection()[0]+1
    year= self.Yearbox.curselection()[0]+1900
    hour= self.Hourbox.curselection()[0]
    minute= self.Minutebox.curselection()[0]
    second=self.Secondbox.curselection()[0]
    if clockobject.setClock(hour, minute, second, month,day,year):
        label2.config(text=f"{clockobject}")
    else:
        label2.config(text="Invalid Date or Time")
        
#Increase day method that calls clock.py to increase the str of the day
def IncreaseDay():
    clockobject.increaseDay()
    label2.config(text=f"{clockobject}")
        
#Decrease day method that calls clock.py to decrease the str of the day           
def DecreaseDay():
    clockobject.decreaseDay()
    label2.config(text=f"{clockobject}")
    
#Increase second method that calls clock.py to increase the str of the second
def Increasesecond():
    clockobject.increaseSecond()
    label2.config(text=f"{clockobject}")    
    
            
#Decrease second method that calls clock.py to decrease the str of the second
def Decreasesecond ():
    clockobject.decreaseSecond()
    label2.config(text=f"{clockobject}")    
        
#Create, size, and place 3 colorful frames to hold the list, button, and scroll widgets 
top_frame=tk.Frame(screen, bg="SkyBlue2", width=699, height=66)
top_frame.place(rely=.02, relx=.25)
middile_frame= tk.Frame(screen, bg="lightblue3", width= 1788, height=433)
middile_frame.place(rely=.13, relx=.0001)
bottom_frame= tk.Frame(screen, bg ="LightSkyBlue3", width= 699, height= 230)
bottom_frame.place(rely=.70, relx=.26)

#Create and place a str that displays the current time that change
label1= tk.Label(screen, text= "Current Time")
label2= tk.Label(screen, text= "01/01/1980 12:00:00 AM")

label1.place(rely=.03, relx=.44)
label2.place(rely=.07, relx=.42)

#Create and place widget lables for the list boxes that will hold the months, days, years, hours, minutes, and seconds
label3= tk.Label(middile_frame, text= "Month")
label3.place(rely=.02, relx=.24)

label3= tk.Label(middile_frame, text= "Day")
label3.place(rely=.02, relx=.33)
        
label3= tk.Label(middile_frame, text= "Year")
label3.place(rely=.02,relx=.38)

label3= tk.Label(middile_frame, text= "Hour")
label3.place(rely=.02, relx=.44)

label3= tk.Label(middile_frame, text= "Minute")
label3.place(rely=.02,relx=.49)

label3= tk.Label(middile_frame, text= "Second")
label3.place(rely=.02, relx=.56)

#Create and place widget buttons that, when pressed, activate thier connected methods 
quitbutton=tk.Button(screen,text="Quit",command=screen.destroy)
quitbutton.place(rely=.85, relx=0.48)

Decreaseday=tk.Button(screen,text="Decrease Day",command=DecreaseDay)
Decreaseday.place(rely=.80, relx=0.45)

Increaseday=tk.Button(screen,text="Increase Day",command=IncreaseDay)
Increaseday.place(rely=.80, relx=0.36)

SetTime=tk.Button(screen,text="Set Time",command=SetClock)
SetTime.place(rely=.80, relx=0.30)


Increasesecond=tk.Button(screen,text="Increase Second",command=Increasesecond)
Increasesecond.place(rely=.80, relx=0.53)

Decreasesecond=tk.Button(screen,text="Decrease Second",command=Decreasesecond)
Decreasesecond.place(rely=.80, relx=0.62)


#Create, size, and place the list box for the months of the year
Month=["January","February","March","April","May","June","July","August","September","October","December"]

Monthbox= tk.Listbox(screen, width=14,exportselection=0,selectmode="single")

for x in range(len(Month)):
    Monthbox.insert("end",Month[x])
scrollbar1=tk.Scrollbar(screen, orient ="vertical")
scrollbar1.config(command=Monthbox.yview)
Monthbox.config(yscrollcommand=scrollbar1.set)






#Create and place the scroll bar for monthbox
Monthbox.place(rely=.17, relx=.26)
scrollbar1.place(rely=.23, relx=.32)

#Create, size, and place the list box for the days of the year
Daybox= tk.Listbox(middile_frame, width=3,exportselection=0,selectmode="single")

for x in range(1,32):
    Daybox.insert("end",[x])
    
#Create and place the scroll bar for daybox
scrollbar2=tk.Scrollbar(screen, orient ="vertical")
scrollbar2.config(command=Daybox.yview)
Daybox.config(yscrollcommand=scrollbar2.set)

scrollbar2.place(rely=.23, relx=.40)
Daybox.place(rely=.07, relx=.33)

#Create, size, and place the list box for the years from 1900 to 2101
Yearbox= tk.Listbox(middile_frame, width=6,exportselection=0,selectmode="single")

for x in range(1900,2101):
    Yearbox.insert("end",[x])

scrollbar3=tk.Scrollbar(screen, orient ="vertical")
scrollbar3.config(command=Daybox.yview)
Yearbox.config(yscrollcommand=scrollbar3.set)

#Create and place it's corresponding scroll box 
scrollbar3.place(rely=.23, relx=.47)
Yearbox.place(rely=.07, relx= .38)

#Create and place the list box for the hours in the day 
Hourbox= tk.Listbox(middile_frame, width=3,exportselection=0,selectmode="single")

for x in range(0,24):
    Hourbox.insert("end",[x])
    
#Create and place it's corresponding scroll box 
Hourbox.config(yscrollcommand=scrollbar3.set)

scrollbar4=tk.Scrollbar(screen, orient ="vertical")
scrollbar4.config(command=Daybox.yview)
Hourbox.config(yscrollcommand=scrollbar4.set)

scrollbar4.place(rely=.23, relx=.53)
Hourbox.place(rely=.07, relx=.44)

#Create, size, and place the list box for the minutes in an hour
Minutebox= tk.Listbox(middile_frame, width=3,exportselection=0,selectmode="single")

for x in range(0,60):
    Minutebox.insert("end",[x])

Minutebox.config(yscrollcommand=scrollbar3.set)

scrollbar5=tk.Scrollbar(screen, orient ="vertical")
scrollbar5.config(command=Minutebox.yview)

#Create and place it's corresponding scroll bar
Minutebox.config(yscrollcommand=scrollbar4.set)

scrollbar5.place(rely=.23, relx=.60)
Minutebox.place(rely=.07, relx=.50)

#Create, size, and place the list box for the seconds in a minute
Secondbox= tk.Listbox(middile_frame, width=3,exportselection=0,selectmode="single")

for x in range(0,60):
    Secondbox.insert("end",[x])

Secondbox.config(yscrollcommand=scrollbar3.set)

#Create and place it's corresponding scroll bar
scrollbar6=tk.Scrollbar(screen, orient ="vertical")
scrollbar6.config(command=Secondbox.yview)
Secondbox.config(yscrollcommand=scrollbar6.set)

scrollbar6.place(rely=.23, relx=.68)
Secondbox.place(rely=.07, relx=.57)
        


        
#Call screen mian loop to process any and all commands for the GUI
screen.mainloop()

        
