from tkinter import *
root = Tk()

root.geometry("1000x70")
root.title("My first App")
root.maxsize(400,700)
root.minsize(100,200)

y = Label(root,text="How are you")
y.pack()

root.mainloop()
