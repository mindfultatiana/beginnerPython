from tkinter import *
import ast

# Creates frame for the calculator
def create_button_frame(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="pink")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

# Creates what a button is
def button(source, side, text, command=None, width=None, height=None):
    storeObj = Button(source, text=text, command=command, width=width, height=height)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'georgia 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        # Creates display for the calculations to show on
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify='right',
              bd=30, bg="pink").pack(side=TOP, expand=YES, fill=BOTH)

        # Creates the clear button on the GUI
        for clearButton in (["C"]):
            erase = create_button_frame(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda storeObj=display, 
                       q=ichar: storeObj.set(''), width=5, height=2)

        # Creates the number buttons on the GUI
        for numButton in ("789/", "456*", "123-"):
            FunctionNum = create_button_frame(self, TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda storeObj=display, 
                       q=iEquals: storeObj.set(storeObj.get() + q), width=5, height=2)

        # Creates the "0", ".", "+", "%" buttons on the same line
        zeroDotPlusPercent = create_button_frame(self, TOP)
        for iEquals in "0.+%":
            if iEquals == "%":
                button(zeroDotPlusPercent, LEFT, iEquals, lambda storeObj=display: 
                       self.calc_percentage(storeObj), width=5, height=2)
            else:
                button(zeroDotPlusPercent, LEFT, iEquals, lambda storeObj=display, 
                       s=iEquals: storeObj.set(storeObj.get() + s), width=5, height=2)

        # Creates the equals button on the GUI
        EqualButton = create_button_frame(self, TOP)
        button(EqualButton, LEFT, "=", lambda storeObj=display: self.calc(storeObj), 
               width=5, height=2)

    # Creates event for when the buttons are pushed
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

## TODO: Look into ast{} documentation and see if it's more effective than eval
## FIXME: Get the percentage to work with addition and subtraction

    # Calculate percentage
    def calc_percentage(self, display):
        try:
            expression = display.get()
            value = (eval(expression))
            percentage = value / 100
            result = percentage
            display.set(result)
        except:
            display.set("ERROR")


# Start the GUI
if __name__ == '__main__':
    app().mainloop()





