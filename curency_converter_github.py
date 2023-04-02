
#####    soham's curency converter  #####

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('500x600')
root.title("Soham's currency converter")
# root.iconbitmap("D:\VS Code\Tkinter\icons8-punisher-128.ico")
root.configure(background="#261316") #261316 ,


# logo 
logo_label = Label(root,text="-- Soham's Converter --",font=('Helvetica',20,"bold"),bg="#fa1d3d",fg="#261316",width=27,height=3)
logo_label.grid(row=0,columnspan=6,pady=10,padx=20)

# amount label
amount_l = Label(root,text="Amount",fg="#51131b",bg="#ece1d0",font=10,width=10)
amount_l.grid(row=1,column=0,columnspan=1,pady=(20,5))

# Entry box 
amount_entry = Entry(root,width=28,font=('Helvetica',20),bg="#eeeee4")
amount_entry.grid(row=2,columnspan=4,pady=8,padx=(30,10))

# label 
cur_l = Label(root,text="From This Currency",fg="#51131b",bg="#ece1d0",font=('Helvetica',16),width=17,anchor=W,height=2)
cur_l.grid(row=3,columnspan=1,column=0,pady=(5,5))

# drop down box
c_list =['USD','INR','EUR','AED']

dropd = ttk.Combobox(root,values=c_list,width=15,font=('Helvetica',20),foreground="#261316")
dropd.current(0)
dropd.bind("<<ComboboxSelected>>")
dropd.grid(row=3,column=1,columnspan=3,padx=(5,0),pady=15)

# label
cur_l = Label(root,text=" To This Currency",fg="#51131b",bg="#ece1d0",font=('Helvetica',16),width=17,anchor=W,height=2)
cur_l.grid(row=4,columnspan=1,column=0,pady=(5,5))

# drop down box
dropd2= ttk.Combobox(root,values=c_list,width=15,font=('Helvetica',20),foreground="#261316")
dropd2.current(0)
dropd2.bind("<<ComboboxSelected>>")
dropd2.grid(row=4,column=1,columnspan=3,padx=(5,0),pady=15)

# functions
def inr(code,amount):
    dict = {'INR':1,'USD':0.0121,'EUR':0.0113,'AED':0.045}
    return float(amount)*dict[code]

def usd(code,amount):
    dict = {'INR':82.75,'USD':1,'EUR':0.93,'AED':3.67}
    return float(amount)*dict[code]

def eur(code,amount):
    dict = {'INR':88.76,'USD':1.07,'EUR':1,'AED':3.98}
    return float(amount)*dict[code]

def aed(code,amount):
    dict = {'INR':22.37,'USD':0.27,'EUR':0.25,'AED':1}
    return float(amount)*dict[code]

# conver function 
def convert():
    if dropd.get() == 'INR':
        currency = inr(dropd2.get(),amount_entry.get())
        result_l.config(text="%.2f"%currency)
    elif dropd.get() == 'USD':
        currency = usd(dropd2.get(),amount_entry.get())
        result_l.config(text="%.2f"%currency)
    elif dropd.get() == 'EUR':
        currency = eur(dropd2.get(),amount_entry.get())
        result_l.config(text="%.2f"%currency)
    elif dropd.get() == 'AED':
        currency = aed(dropd2.get(),amount_entry.get())
        result_l.config(text="%.2f"%currency)
# button
bt = Button(root,text=' CONVERT ',font=('Helvetica',20),cursor="exchange"
            ,width=15,bd=3,bg="#fa1d3d",fg="black",command=convert)
bt.grid(row=5,columnspan=4,pady=(20,0))

# label
result_l = Label(root,text="--",width=15,font=('Helvetica',35,'bold'),height=1,fg="#261316",bg='#ece1d0')
result_l.grid(row=6,columnspan=4,pady=(25,0),padx=(10,0))


root.mainloop()