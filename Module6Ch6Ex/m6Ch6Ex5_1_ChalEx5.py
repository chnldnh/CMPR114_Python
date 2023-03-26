
#m6Ch6Ex5_1ChalEx5

import tkinter as tk 
from tkinter import messagebox
win = tk.Tk()
win.geometry("350x170")
win.title("Customer Information")
          
lblLastname = tk.Label(win, text="enter the lastname").grid(column = 0, row = 0)
lblFirstname = tk.Label(win, text="enter the firstname").grid(column = 0, row = 1)
lblAddress = tk.Label(win, text="enter the address").grid(column = 0, row = 2)
lblState = tk.Label(win, text="enter the city").grid(column = 0, row = 3)
lblCity = tk.Label(win, text="enter the state").grid(column = 0, row = 4)
lblZipcode = tk.Label(win, text="enter the zipcode").grid(column = 0, row = 5)

def write():
    text_file = open("C:\\Customers.txt", "a")
    content = text_file.write("\nConfirmation: " + str(LN.get()) + ", " + str(FN.get()) + "\n" + str(AD.get()) + "\n" + str(CI.get()) + ", " + str(ST.get()) + " " + str(ZI.get()))
    text_file.close()
    messagebox.showinfo("information", "Data Recorded")

def quit():
    messagebox.showinfo("information", "Thank you...")
    win,destroy()

def submit():
    message.showinfo("information", "entered :" + LN.get() + "," + FN.get() + "," + AD.get() + "," + CI.get() + "," + ST.get() + "," + ZI.get())

LN = tk.StringVar()
txtLastname = tk.Entry(win, width = 12, textvariable = LN).grid(column = 1, row = 0)
FN = tk.StringVar()
txtFirstname = tk.Entry(win, width = 12, textvariable = FN).grid(column = 1, row = 1)
AD = tk.StringVar()
txtAddress = tk.Entry(win, width = 12, textvariable = AD).grid(column = 1, row = 2)
CI = tk.StringVar()
txtCity = tk.Entry(win, width = 12, textvariable = CI).grid(column = 1, row = 3)
ST = tk.StringVar()
txtState = tk.Entry(win, width = 12, textvariable = ST).grid(column = 1, row = 4)
ZI = tk.StringVar()
txtZipcode = tk.Entry(win, width = 12, textvariable = ZI).grid(column = 1, row = 5)

btnSubmit = tk.Button(win, text = "submit", command = submit).grid(column = 0, row = 7)

btnQuit = tk.Button(win, text = "quit", command = quit).grid(column = 1, row = 7)

btnWrite = tk.Button(win, text = "transfer", command = write).grid(column = 2, row = 7)

win.mainloop()
submit()


