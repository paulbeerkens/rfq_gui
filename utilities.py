from tkinter import *
#from tkinter.ttk import Combobox

def callback(sv):
    print (sv.get())

class LabelEntry(Frame):
    def __init__(self, parent, text,command=None):
        super().__init__(parent)
        #self.pack(fill=X)

        lbl = Label(self, text=text, anchor='w')
        lbl.pack(side=LEFT, padx=3, pady=5)

        #self.symbol=StringVar()
        #entry=Combobox(self,textvariable=self.symbol,width=5)
        #entry ['values']=['SPY','EWA','EWB','FXI']

        #self.sv = StringVar()
        #sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
        #entry = Entry(self, width=5, textvariable=self.sv)

        self.entry = Entry(self,width=6)
        self.entry.bind('<Return>', command)
        self.entry.pack(side=LEFT, fill=X, padx=3)

class LabelOptionMenu(Frame):
    def __init__(self,parent,text):
        super().__init__(parent)
        #self.pack()

        lbl = Label(self, text=text, anchor='w')
        lbl.pack(side=LEFT, padx=3, pady=5)

        desk_list=['All','Domestic','Emerging']
        self.values=StringVar()
        self.values.set(desk_list[0])
        dropdown=OptionMenu(self,self.values,*desk_list)
        dropdown.config(width=8)
        dropdown.pack(side=LEFT, padx=3)
