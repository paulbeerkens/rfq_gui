from tkinter import *
from utilities import *

def on_symbol_change(event):
    #print(symbol.sv.get())
    print(symbol.entry.get())


root = Tk()
root.title("RFQ Pricing Viewer")

symbol_frame = LabelFrame(root, text='symbol selection', padx=5, pady=5)
active_rfq_frame = LabelFrame(root, text='Active RFQs', padx=5, pady=5)
pricing_frame = LabelFrame(root, text='Pricing params', padx=5, pady=5)
error_frame = LabelFrame(root, text='Errors', padx=5, pady=5)

symbol_frame.grid(row=0, column=0, padx=10, pady=10)
active_rfq_frame.grid(row=0, column=1, padx=10, pady=10)
pricing_frame.grid(row=0, column=2, padx=10, pady=10)
error_frame.grid(row=0, column=3, padx=10, pady=10)

symbol=LabelEntry(symbol_frame,"Symbol",on_symbol_change)
desk=LabelOptionMenu(symbol_frame,"Desk")
switch_on_rfq_val = StringVar()
switch_on_rfq  = Checkbutton(symbol_frame, text='Switch on RFQ',
        variable=switch_on_rfq_val, onvalue='yes', offvalue='no')


symbol.pack(side=LEFT, padx=3, pady=5)#grid (row=0, column=0)
desk.pack(side=LEFT, padx=10, pady=5)#grid(row=0,column=1)
switch_on_rfq.pack (side=LEFT, padx=3, pady=5)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root.mainloop()
