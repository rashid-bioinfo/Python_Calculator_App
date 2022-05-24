from tkinter import *
from turtle import left


def click(event):
    global scvalue
    # event.widget will return the button which is clicked
    # cget function is used to get the text of button
    text = event.widget.cget("text")
    
    if text == "=":
        if (scvalue.get().isdigit()):
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update( )
    else: 
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("500x600")
root.title("Calculator")


# Frame 1
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold", width=12)
screen.pack(fill=X, ipadx=10, ipady=2, padx=10)

# Frame for calculator buttons 7, 8, 9
f = Frame(root, bg="grey")
b = Button (f, text="9", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button (f, text="8", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button (f, text="7", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

# Frame for calculator buttons 6, 5, 4
f = Frame(root, bg="grey")
b = Button (f, text="6", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button (f, text="5", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button (f, text="4", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

#  Frame for calculator buttons 3, 2, 1
f = Frame(root, bg="grey")
b = Button (f, text="3", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button (f, text="2", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button (f, text="1", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

#  Frame for calculator buttons 0, -, *
f = Frame(root, bg="grey")
b = Button (f, text="0", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=21, pady=5)
b.bind("<Button-1>", click)

b = Button (f, text="-", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=21, pady=5)
b.bind("<Button-1>", click)

b = Button (f, text="*", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=21, pady=5)
b.bind("<Button-1>", click)

f.pack()

#  Frame for calculator buttons /, %, =
f = Frame(root, bg="grey")
b = Button (f, text="/", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=16, pady=5)
b.bind("<Button-1>", click)

b = Button (f, text="%", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=16, pady=5)
b.bind("<Button-1>", click)

b = Button (f, text="=", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=16, pady=5)
b.bind("<Button-1>", click)

f.pack()

#  Frame for calculator buttons C, %, =
f = Frame(root, bg="grey")
b = Button (f, text="C", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=16, pady=5)
b.bind("<Button-1>", click)

b = Button (f, text="  ", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=16, pady=5)
b.bind("<Button-1>", click)

b = Button (f, text="  ", padx= 25, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=16, pady=5)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()