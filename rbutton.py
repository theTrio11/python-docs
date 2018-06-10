#types of button
import tkinter as tk
root=tk.Tk()
v=tk.IntVar()
tk.Label(root,text="""choose colour:""",
         justify=tk.LEFT,
         padx=20).pack()
tk.Radiobutton(root,
               text="pink",
               padx=20,
               variable=v,
               bg="pink",
               value=1).pack(anchor=tk.W)
tk.Radiobutton(root,
               text="blue",
               padx=20,
               variable=v,
               bg="blue",
               value=2).pack(anchor=tk.W)
