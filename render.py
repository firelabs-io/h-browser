import tkinter # fuck it, no one cares about this browser lol

def loop(root):
    root.mainloop()
def pc(root, text): # <p>
    label = tkinter.Label(root, text=text, wraplength=400, anchor="w", justify="left")
    label.pack(padx=10, pady=5, anchor="w")
def inpc(root): # <input>
    entry = tkinter.Entry(root)
    entry.pack(padx=10, pady=5, anchor="w")
    entry.bind("<Return>", None)
def h1c(root, text): # <h1>
    label = tkinter.Label(root, text=text, font=("Helvetica", 18, "bold"), anchor="w")
    label.pack(padx=10, pady=10, anchor="w")
def initgui():
    root = tkinter.Tk()
    root.geometry('800x800')
    return root
