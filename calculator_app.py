from tkinter import *

btn_cli = 0


def click(event):
    text = event.widget.cget("text")
    if value.get() == "Error":
        value.set("")
    global btn_cli
    if btn_cli == 0:
        value.set("")
        btn_cli += 1
    if text == "=":
        if value.get().isdigit():
            value.set(value)
        elif "%" in value.get():
            try:
                list1 = value.get().split("%")
                value.set(str((float(list1[0]) * float(list1[1])) / 100))
            except:
                value.set("Error")
        else:
            try:
                value.set(eval(value.get()))
                textarea.update()
            except:
                value.set("Error")

    elif text == "←":
        value.set(value.get()[:-1])
    elif text == "C":
        value.set("")
        textarea.update()

    else:
        if text == ".":
            value.set(value.get() + text)
        else:
            value.set(value.get() + text)
            textarea.update()


window = Tk()
window.geometry("300x450")
window.iconbitmap("icon.ico")
window.minsize(240, 450)
window.title("Calculator by Parjanya")
value = StringVar()
value.set("")
textarea = Entry(window, textvar=value, font="Sans-serif 30")
textarea.insert(0, "0")
textarea.config(state=DISABLED)
textarea.pack(fill=X, ipadx=8, pady=10, padx=10)

frame = Frame(window)

x = 9

btn = Button(frame, text="+", font="Sans-serif 20")
btn.pack(side="left", ipadx=11, ipady=10, padx=1)
btn.bind("<Button-1>", click)

btn = Button(frame, text="-", font="Sans-serif 20")
btn.pack(side="left", ipadx=12, ipady=10, padx=1)
btn.bind("<Button-1>", click)

btn = Button(frame, text="/", font="Sans-serif 20")
btn.pack(side="left", ipadx=13, ipady=10, padx=1)
btn.bind("<Button-1>", click)

btn = Button(frame, text="*", font="Sans-serif 20")
btn.pack(side="left", ipadx=12, ipady=10, padx=1)
btn.bind("<Button-1>", click)

frame.pack(pady=1)

for i in range(3):
    frame = Frame(window)
    for j in range(4):
        if x >= 0:
            text = x
        if x == -1:
            text = "."
        if x == -2:
            text = "%"
        btn = Button(frame, text=f"{text}", font="Sans-serif 20")
        btn.pack(side="left", ipadx=10, ipady=10, padx=1)
        btn.bind("<Button-1>", click)

        x -= 1

    frame.pack(pady=1)

frame = Frame(window)

btn = Button(frame, text="C", font="Sans-serif 20")
btn.pack(side="left", ipadx=10, ipady=10, padx=1)
btn.bind("<Button-1>", click)

btn = Button(frame, text="←", font="Sans-serif 20")
btn.pack(side="left", ipadx=10, ipady=10, padx=1)
btn.bind("<Button-1>", click)

btn = Button(frame, text="=", bg="orange", font="Sans-serif 20")
btn.pack(side="left", ipadx=33, ipady=10, padx=1)
btn.bind("<Button-1>", click)

frame.pack(pady=1)

window.mainloop()
