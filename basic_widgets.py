from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)
#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()


#Buttons
def action():
    print("Do something")


"""
calls action() when pressed.
text="Click Me" it will be written on the button.
the command attribute is used to trigger when the user will click the button and action() will get executed.
"""
button = Button(text="Click Me", command=action)
# To put button the screen it should have layout and that layout is given by using pack()
button.pack()


# Asking for user input of width 30, and we can also leave as it is
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
"""
get() is used in order to fetch the actual value the user feed.
When the by default string(string="Some text to begin with.") is not given then even when we write something in the 
entry box nothing gets printed on the console.
"""
print(entry.get())
entry.pack()

#Text Box
#It is used to create TextBox height represent number of lines and width represents the width of the box
text = Text(height=5, width=30)
#focus() is used to put cursor in textbox.
text.focus()
#Adds some text to begin with.
# END is just an index to allow tkinter to figure out what particular item we're referring to, and we don't have to
# change it ever this is just the code we have to use always, and it will never be changed
text.insert(END, "Example of multi-line text entry.")
#Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


#Spinbox is just like a small box from where we can give numbers by clicking up and down key on the spin button
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())


# We can specify the initial value and the ending value and everytime when the user clicked upper or lower key
# spinbox_used get triggered using command attribute
spinbox = Spinbox(from_=-5, to=10, width=5, command=spinbox_used)
spinbox.pack()


#Scale
#Called with current scale value.
def scale_used(value):
    print(value)


#It actually passes the over the value in which the scale is currently on. Here also command behaves like event listener
#in turtle
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


#variable to hold on to checked state, 0 is off, 1 is on.
#The variable checked_state is something that is defined by the tkinter module as an IntVar() and this is a class
#And once we create object from that class then we can add it to our check button when we create it and that variable
#will keep track of the value of that checkbox 1 for on and 0 for off.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
#checked_state.get()
checkbutton.pack()


#Radiobutton:- Radiobutton are useful to pick between any two different options. So normally we have a number of options
#and only one of them can be selected at any one time
def radio_used():
    print(radio_state.get())


#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
#We give value to each button i.e. for radio1 we give value=1 and for radio2 we give value=2 so when radio1 button is
#selected 1 gets printed using radio_used() and when radio2 button is clicked 2 gets printed on the console
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox:- Listbox is a list of options created from python list
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
#We use bind() to call this particular call this particular call back.This way whenever any of the items in here, it
#will print out and get the current selection
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
"""
A lot of the code is pretty much going to be used same in each time.So it doesn't really matter if we don't understand 
fully exactly what some of these weird components are. It just a factor how this tkinter library has taken this tk 
module and turned it into a Python format for us to be able to interact with it using Python.
"""
window.mainloop()
