import tkinter
from tkinter import BOTH, RIGHT, END, DISABLED, NORMAL


#Define window
root = tkinter.Tk()
root.title("Calculator")
root.iconbitmap('calc.ico')
root.geometry('300x400')
root.resizable(0,0)




#colors
dark_green = "#93af22"
light_green = "#acc253"
white_green = "#edefe0"
button_font = ("Arial", 18)
display_font = ('Arial', 30)


#Define functions
def submit_number(number):
    '''Add a number or decimal to the display'''
    #Get the current value of the display and then delete the value from the entry display
    value = display.get()
    display.delete(0, END)
    
    #Update the display expression by concatenating the new button pressed.
    display_expression = value + str(number)
    display.insert(0, display_expression)

    #If decimal was pressed, disable so it cannot be pressed twice
    if "." in display.get():
        decimal_button['state'] = DISABLED



def operate(operator):
    """Store the first number of the expression and the operation to be used"""
    global first_number
    global operation

    #Get the operator pressed and current value of the display.  This is the first number in a calculation
    operation = operator
    first_number = display.get()

    #Delete the value (first_number) from the entry display
    display.delete(0, END)

    #Return decimal button state to normal
    decimal_button['state'] = NORMAL

    #Disable all operator buttons until equal or clear is pressed
    add_button['state'] = DISABLED
    subtract_button['state'] = DISABLED
    multiply_button['state'] = DISABLED
    divide_button['state'] = DISABLED
    exponent_button['state'] = DISABLED
    inverse_button['state'] = DISABLED
    square_button['state'] = DISABLED


def equal():
    """Run the stored operation for two numbers; first_number and the current number in the entry"""
    #Perform the desired mathematics
    if operation == "add":
        value = float(first_number) + float(display.get())
    elif operation == "subtract":
        value = float(first_number) - float(display.get())
    elif operation == 'multiply':
        value = float(first_number) * float(display.get())
    elif operation == 'divide':
        if display.get() == "0":
            value = "ERROR"
        else:
            value = float(first_number) / float(display.get())
    elif operation == 'exponent':
        value = float(first_number) ** float(display.get())

    #Remove the current value of the display and update it with the result of the operation        
    display.delete(0, END)
    display.insert(0, value)

    #Return button states to normal
    enable_buttons()


def enable_buttons():
    """Enable all buttons on the calculator"""
    decimal_button['state'] = NORMAL
    add_button['state'] = NORMAL
    subtract_button['state'] = NORMAL
    multiply_button['state'] = NORMAL
    divide_button['state'] = NORMAL
    exponent_button['state'] = NORMAL
    inverse_button['state'] = NORMAL
    square_button['state'] = NORMAL



def clear():
    """Clear the display"""
    display.delete(0, END)

    #Return button states to normal
    enable_buttons()
    

def inverse():
    """Calculate the inverse of a given value"""
    #Do not allow for 1/0
    if display.get() == "0":
        value = 'ERROR'
    else:
        value = 1/float(display.get())

    #Remove the current value of the display and update it with the result of the operation
    display.delete(0, END)
    display.insert(0, value)

    #Return decimal button state to normal
    decimal_button['state'] = NORMAL


def square():
    """Calculate the square of a given value"""
    value = float(display.get())**2
    
    #Remove the current value of the display and update it with the result of the operation
    display.delete(0, END)
    display.insert(0, value)   

    #Return decimal button state to normal
    decimal_button['state'] = NORMAL


def negate():
    """Negate a given value"""
    value = -1*float(display.get())

    #Remove the current value of the display and update it with the result of the operation
    display.delete(0, END)
    display.insert(0, value)









#GUI Layout
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.pack(padx=2, pady=(5,20))
button_frame.pack(padx=2, pady=2, fill=BOTH, expand=True)

#layout for display frame
display = tkinter.Entry(display_frame, width=50, font=display_font, bg=white_green, borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)


#layout for button frame
clear_button = tkinter.Button(button_frame, text="Clear", font=button_font, bg=dark_green, command=clear)
quit_button = tkinter.Button(button_frame, text="Quit", font=button_font, bg=dark_green, command=root.destroy)

inverse_button = tkinter.Button(button_frame, text="1/x", font=button_font, bg=light_green, command=inverse)
square_button = tkinter.Button(button_frame, text="x^2", font=button_font, bg=light_green, command=square)
exponent_button = tkinter.Button(button_frame, text="x^n", font=button_font, bg=light_green, command=lambda:operate("exponent"))
divide_button = tkinter.Button(button_frame, text=" / ", font=button_font, bg=light_green, command=lambda:operate("divide"))
multiply_button = tkinter.Button(button_frame, text="*", font=button_font, bg=light_green, command=lambda:operate("multiply"))
subtract_button = tkinter.Button(button_frame, text="-", font=button_font, bg=light_green, command=lambda:operate("subtract"))
add_button = tkinter.Button(button_frame, text="+", font=button_font, bg=light_green, command=lambda:operate("add"))
equal_button = tkinter.Button(button_frame, text="=", font=button_font, bg=dark_green, command=equal)
decimal_button = tkinter.Button(button_frame, text=".", font=button_font, fg="white", bg="black", command=lambda:submit_number("."))
negate_button = tkinter.Button(button_frame, text="+/-", font=button_font, fg="white", bg="black", command=negate)

nine_button = tkinter.Button(button_frame, text="9", font=button_font, fg="white", bg="black", command=lambda:submit_number(9))
eight_button = tkinter.Button(button_frame, text="8", font=button_font, fg="white", bg="black", command=lambda:submit_number(8))
seven_button = tkinter.Button(button_frame, text="7", font=button_font, fg="white", bg="black", command=lambda:submit_number(7))
six_button = tkinter.Button(button_frame, text="6", font=button_font, fg="white", bg="black", command=lambda:submit_number(6))
five_button = tkinter.Button(button_frame, text="5", font=button_font, fg="white", bg="black", command=lambda:submit_number(5))
four_button = tkinter.Button(button_frame, text="4", font=button_font, fg="white", bg="black", command=lambda:submit_number(4))
three_button = tkinter.Button(button_frame, text="3", font=button_font, fg="white", bg="black", command=lambda:submit_number(3))
two_button = tkinter.Button(button_frame, text="2", font=button_font, fg="white", bg="black", command=lambda:submit_number(2))
one_button = tkinter.Button(button_frame, text="1", font=button_font, fg="white", bg="black", command=lambda:submit_number(1))
zero_button = tkinter.Button(button_frame, text="0", font=button_font, fg="white", bg="black", command=lambda:submit_number(0))

#First row
clear_button.grid(row=0, column=0, columnspan=2, sticky="WE", pady=1)
quit_button.grid(row=0, column=2, columnspan=2, sticky="WE", pady=1)
#Second row
inverse_button.grid(row=1, column=0, sticky="WE", pady=1)
square_button.grid(row=1, column=1, sticky="WE", pady=1)
exponent_button.grid(row=1, column=2, sticky="WE", pady=1)
divide_button.grid(row=1, column=3, sticky="WE", pady=1)
#Thrid row (Add padding to create size of columns)
seven_button.grid(row=2, column=0, sticky="WE", pady=1, ipadx=20)
eight_button.grid(row=2, column=1, sticky="WE", pady=1, ipadx=20)
nine_button.grid(row=2, column=2, sticky="WE", pady=1, ipadx=20)
multiply_button.grid(row=2, column=3, sticky="WE", pady=1, ipadx=20)
#Forth Row 
four_button.grid(row=3, column=0, sticky="WE", pady=1)
five_button.grid(row=3, column=1, sticky="WE", pady=1)
six_button.grid(row=3, column=2, sticky="WE", pady=1)
subtract_button.grid(row=3, column=3, sticky="WE", pady=1)
#Fifth Row
one_button.grid(row=4, column=0, sticky="WE", pady=1)
two_button.grid(row=4, column=1, sticky="WE", pady=1)
three_button.grid(row=4, column=2, sticky="WE", pady=1)
add_button.grid(row=4, column=3, sticky="WE", pady=1)
#Six Row 
negate_button.grid(row=5, column=0, sticky="WE", pady=1)
zero_button.grid(row=5, column=1, sticky="WE", pady=1)
decimal_button.grid(row=5, column=2, sticky="WE", pady=1)
equal_button.grid(row=5, column=3, sticky="WE", pady=1)

#Run the root window's main loop
root.mainloop()
