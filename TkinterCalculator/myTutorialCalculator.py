from tkinter import *

# Create frame for the calculator
def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="pink")
    storeObj.pack(side=side, expand=YES, fill = BOTH)
    return storeObj

# Create the Button
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'georgia 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

# Create display for the calculations to show on   
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify='right', 
              bd=30, bg="pink").pack(side=TOP, expand=YES, fill=BOTH)

# Create the clear button on the GUI
        for clearButton in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                       storeObj=display, q=ichar: storeObj.set(''))

# Create the number buttons on the GUI                
        for numButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = iCalc(self, TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda
                       storeObj=display, q=iEquals: storeObj.set(storeObj.get() + q))

# Create the equals button on the GUI               
        EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == "=":
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self, 
                                storeObj=display: s.calc(storeObj), '+')
                
            else:
               btniEquals = button(EqualButton, LEFT, iEquals, lambda storeObj=display,
                                   s=' %s ' % iEquals: storeObj.set(storeObj.get() + s))
               
# Create event for when the buttons are pushed
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR") 
        


# Start the GUI
if __name__=='__main__':
    app().mainloop()