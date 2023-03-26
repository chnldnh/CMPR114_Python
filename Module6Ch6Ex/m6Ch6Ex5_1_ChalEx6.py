
#m6Ch6Ex5_1ChalEx6

import tkinter as tk 
from tkinter import messagebox
win = tk.Tk()
win.geometry("300x100")
win.title("Sum Average Total")
          
lbl1Num = tk.Label(win, text="enter the 1st number").grid(column = 0, row = 0)
lbl2Num = tk.Label(win, text="enter the 2nd number").grid(column = 0, row = 1)
lbl3Num = tk.Label(win, text="enter the 3rd number").grid(column = 0, row = 2)


def write():
    text_file = open("C:\\Number.txt", "a")

    firstNumm = int(firstNum.get())
    secondNumm = int(secondNum.get())
    thirdNumm = int(thirdNum.get())
    calSum = (firstNumm + secondNumm + thirdNumm)
    calAvg = (calSum / 3.0)
    text_file.write("\nThe three numbers are: " + str(firstNumm) + ", " + str(secondNumm) + " and " + str(thirdNumm) + "\nThe total is " + 
                    str(calSum) + "\nThe average is " + str(calAvg))
    text_file.write()
    text_file.close()
    messagebox.showinfo("information", "Data Recorded")

def quit():
    messagebox.showinfo("information", "Thank you...")
    win,destroy()

def submit():
    messagebox.showinfo("information", "entered :" + firstNum.get() + "," + secondNum.get() + "," + thirdNum.get() + "," + calSum.get() + "," + calAvg.get())

firstNum = tk.StringVar()
txtFirstNum = tk.Entry(win, width = 12, textvariable = firstNum).grid(column = 1, row = 0)
secondNum = tk.StringVar()
txtSecondNum = tk.Entry(win, width = 12, textvariable = secondNum).grid(column = 1, row = 1)
thirdNum = tk.StringVar()
txtThirdNum = tk.Entry(win, width = 12, textvariable = thirdNum).grid(column = 1, row = 2)

btnSubmit = tk.Button(win, text = "submit", command = submit).grid(column = 0, row = 7)

btnQuit = tk.Button(win, text = "quit", command = quit).grid(column = 1, row = 7)

btnWrite = tk.Button(win, text = "transfer", command = write).grid(column = 2, row = 7)

win.mainloop()
submit()