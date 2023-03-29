
# m7ClassEx7a_project3
# Create list box using tkinter

from tkinter import*

root  = Tk()

listbox = Listbox(root, width=40, height=10, selectmode=MULTIPLE)

root.geometry('180x200')

label = Label(root, text = ' FOOD ITEMS')

listbox.insert(1, "Data Structure")
listbox.insert(2, "Algorithm")
listbox.insert(3, "Data Science")
listbox.insert(4, "Machine Learning")
listbox.insert(5, "Blockchain")

def selected_item():
    for i in listbox.curselection():
        print(listbox.get(i))

btn = Button(root, text = 'Print Selected', command = selected_item)

btn.pack(side = 'bottom')

listbox.pack()
root.mainloop()


