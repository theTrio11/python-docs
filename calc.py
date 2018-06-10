import tkinter as tk
a = tk.Tk()
variable1 = tk.IntVar()
variable2 = tk.IntVar()
res=tk.IntVar()
def add():
    x = variable1.get()
    y = variable2.get()
    res=x+y
    label3=tk.Label(a,text=str(res),padx=20).pack()

def div():
    x = variable1.get()
    y = variable2.get()
    res=x/y
    label3=tk.Label(a,text=str(res),padx=20).pack()

def powe():
    x = variable1.get()
    y = variable2.get()
    res=x**y
    label3=tk.Label(a,text=str(res),padx=20).pack()

a.title("Calculator")
label1 = tk.Label(a, text="Enter The First Number",
                      padx=20).pack()
field1 = tk.Entry(a, textvariable=variable1).pack()
label2 = tk.Label(a, text="Enter the second number",
                      padx=20).pack()
field2 = tk.Entry(a, textvariable=variable2).pack()
button1 = tk.Button(a,
                    text="Add",
                    pady=4,
                    justify=tk.RIGHT,
                    command=add).pack()
button2 = tk.Button(a,
                    text="divison",
                    pady=4,
                    justify=tk.RIGHT,
                    command=div).pack()
button3 = tk.Button(a,
                    text="pow",
                    pady=4,
                    justify=tk.RIGHT,
                    command=powe).pack()
label3=tk.Label(a,text=str(res),padx=20).pack()
a.mainloop()    
