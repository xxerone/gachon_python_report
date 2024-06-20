#p432-433 calculator2
from math import *
from tkinter import *

window = Tk()
window.title("My Calculator")
display = Entry(window, width=33, bg = "yellow")
display.grid(row = 0, column = 0, columnspan = 5)
button_list = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', ' ', 
    '1', '2', '3', '-', ' ',
    '0', '.', '=', '+', 'sin',
]

def click(key):
    if key == "=":
        result = eval(display.get()) #일반적인 부분에 대한 계산은 eval / display.get()은 entry 부분에서 
        s = str(result)
        display.insert(END, "=" + s)
    #if key == "sin":


#def sin(t):
#    result = eval(display.get()) #일반적인 부분에 대한 계산은 eval / display.get()은 entry 부분에서 
#    s = str(result)
#    display.insert(END, "=" + s)

#Button(window, text = 'sin', command = lambda:sin(display.get()))

row_index = 1
col_index = 0
for button_text in button_list:
    Button(window, text = button_text, width = 5, 
           command=lambda t=button_text: click(t)).grid(
               row = row_index, column = col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0
window.mainloop()
